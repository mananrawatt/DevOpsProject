from flask import Flask, jsonify
import requests

app = Flask(__name__)


@app.route('/health', methods=['GET'])
def health_check():
    # Simulate health check logic
    return jsonify({"status": "Application is live", "status_code": 200}), 200


@app.route('/test', methods=['GET'])
def test_endpoint():
    # Simulate a test endpoint
    return jsonify({"message": "Application is working fine", "status_code": 200}), 200


@app.route('/status', methods=['GET'])
def status_check():
    # Example: Check Jenkins server
    try:
        response = requests.get("http://localhost:8080", timeout=5)
        jenkins_status = response.status_code
    except Exception as e:
        jenkins_status = f"Jenkins is not reachable: {str(e)}"

    # Example: Check Kubernetes cluster (just simulating here)
    k8s_status = "Cluster is running"  # Simulate logic here, like checking Kubernetes status

    # You can extend this to check other components like databases, services, etc.

    return jsonify({
        "jenkins_status": jenkins_status,
        "k8s_status": k8s_status
    }), 200


if __name__ == '__main__':
    app.run(port=5001)  # Running Flask on port 5001
