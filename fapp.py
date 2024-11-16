from flask import Flask, jsonify
import jenkins_status
import kubernetes_details
# import minikube_status

app = Flask(__name__)

@app.route('/health/home', methods=['GET'])
def home_health():
    # Check the home section (just an example, you can add more complex checks)
    return jsonify(status="OK", message="Home section is running"), 200

@app.route('/health/jenkins', methods=['GET'])
def jenkins_health():
    # Check Jenkins status (e.g., ping Jenkins API or check pipeline)
    try:
        result = jenkins_status.get_pipeline_status()  # Assuming you have a function like this
        if result == "success":
            return jsonify(status="OK", message="Jenkins is healthy"), 200
        else:
            return jsonify(status="Fail", message="Jenkins is not responding properly"), 503
    except Exception as e:
        return jsonify(status="Fail", message=f"Jenkins error: {str(e)}"), 503

@app.route('/health/k8s', methods=['GET'])
def k8s_health():
    # Check Kubernetes status (check if cluster and pods are healthy)
    try:
        result = kubernetes_details.check_cluster_health()  # Add your own check
        if result == "healthy":
            return jsonify(status="OK", message="Kubernetes is healthy"), 200
        else:
            return jsonify(status="Fail", message="Kubernetes cluster issue"), 503
    except Exception as e:
        return jsonify(status="Fail", message=f"Kubernetes error: {str(e)}"), 503

@app.route('/health/minikube', methods=['GET'])
def minikube_health():
    # Check Minikube status
    try:
        result = minikube_status.check_status()  # Add your own check function here
        if result == "running":
            return jsonify(status="OK", message="Minikube is running"), 200
        else:
            return jsonify(status="Fail", message="Minikube is not running properly"), 503
    except Exception as e:
        return jsonify(status="Fail", message=f"Minikube error: {str(e)}"), 503

if __name__ == '__main__':
    app.run(debug=True, port=5002)  # Flask runs on port 5001 by default














#
# from flask import Flask, jsonify
# import requests
#
# app = Flask(__name__)
#
#
# @app.route('/health', methods=['GET'])
# def health_check():
#     # Simulate health check logic
#     return jsonify({"status": "Application is live", "status_code": 200}), 200
#
#
# @app.route('/test', methods=['GET'])
# def test_endpoint():
#     # Simulate a test endpoint
#     return jsonify({"message": "Application is working fine", "status_code": 200}), 200
#
#
# @app.route('/status', methods=['GET'])
# def status_check():
#     # Example: Check Jenkins server
#     try:
#         response = requests.get("http://localhost:8080", timeout=5)
#         jenkins_status = response.status_code
#     except Exception as e:
#         jenkins_status = f"Jenkins is not reachable: {str(e)}"
#
#     # Example: Check Kubernetes cluster (just simulating here)
#     k8s_status = "Cluster is running"  # Simulate logic here, like checking Kubernetes status
#
#     # You can extend this to check other components like databases, services, etc.
#
#     return jsonify({
#         "jenkins_status": jenkins_status,
#         "k8s_status": k8s_status
#     }), 200
#
#
# if __name__ == '__main__':
#     app.run(port=5001)  # Running Flask on port 5001
