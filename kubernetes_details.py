# from kubernetes import client, config
# import logging
# import streamlit as st
#
# # Configure logging
# logging.basicConfig(level=logging.DEBUG)
#
# # Load Kubernetes configuration
# def load_kubernetes_config():
#     try:
#         config.load_kube_config()
#         logging.debug("Kubernetes configuration loaded successfully.")
#     except Exception as e:
#         logging.error(f"Error loading Kubernetes configuration: {e}")
#         st.error(f"Error loading Kubernetes configuration: {e}")
#
# # Function to get all namespaces in the cluster
# def list_namespaces():
#     try:
#         v1 = client.CoreV1Api()
#         namespaces = v1.list_namespace()
#         return [ns.metadata.name for ns in namespaces.items]
#     except client.exceptions.ApiException as e:
#         logging.error(f"Error listing namespaces: {e}")
#         st.error(f"Error listing namespaces: {e}")
#         return []
#
# # Function to get all pods in a selected namespace
# def list_pods(namespace="default"):
#     try:
#         v1 = client.CoreV1Api()
#         pods = v1.list_namespaced_pod(namespace=namespace)
#         return [pod.metadata.name for pod in pods.items]
#     except client.exceptions.ApiException as e:
#         logging.error(f"Error listing pods in namespace '{namespace}': {e}")
#         st.error(f"Error listing pods in namespace '{namespace}': {e}")
#         return []
#
# # Function to get Kubernetes pod logs
# def get_pod_logs(pod_name, namespace="default"):
#     try:
#         v1 = client.CoreV1Api()
#         pod_name = pod_name.strip()
#         logs = v1.read_namespaced_pod_log(name=pod_name, namespace=namespace)
#         return logs
#     except client.exceptions.ApiException as e:
#         return f"Error: {e.reason}. Details: {e.body}"
#
# # Function to describe a Kubernetes pod
# def describe_pod(pod_name, namespace="default"):
#     try:
#         v1 = client.CoreV1Api()
#         pod_name = pod_name.strip()
#         pod = v1.read_namespaced_pod(name=pod_name, namespace=namespace)
#         return str(pod)
#     except client.exceptions.ApiException as e:
#         return f"Error: {e.reason}. Details: {e.body}"
#
# # Function to create the Streamlit interface for Kubernetes interaction (this will be called from app.py)
# def kubernetes_ui():
#     st.title("Kubernetes Pod Details Viewer")
#
#     # Load Kubernetes configuration
#     load_kubernetes_config()
#
#     # Fetch and display available namespaces
#     namespaces = list_namespaces()
#
#     if not namespaces:
#         st.error("No namespaces found.")
#         return
#
#     # Namespace selection dropdown
#     selected_namespace = st.selectbox("Select Namespace", namespaces, index=0)
#     st.write(f"Selected Namespace: {selected_namespace}")
#
#     # List pods in the selected namespace
#     pods = list_pods(selected_namespace)
#
#     if pods:
#         selected_pod = st.selectbox("Select Pod", pods, index=0)
#         st.write(f"Selected Pod: {selected_pod}")
#
#         # Option to either describe pod or view logs
#         action = st.radio("Action", ("Describe Pod", "View Pod Logs"))
#
#         if action == "Describe Pod":
#             pod_description = describe_pod(selected_pod, selected_namespace)
#             st.subheader("Pod Description")
#             st.text(pod_description)
#
#         elif action == "View Pod Logs":
#             pod_logs = get_pod_logs(selected_pod, selected_namespace)
#             st.subheader("Pod Logs")
#             st.text(pod_logs)
#     else:
#         st.write(f"No pods found in namespace '{selected_namespace}'.")





from kubernetes import client, config
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG)

# Load Kubernetes configuration
def load_kubernetes_config():
    try:
        config.load_kube_config()
        logging.debug("Kubernetes configuration loaded successfully.")
    except Exception as e:
        logging.error(f"Error loading Kubernetes configuration: {e}")

# Function to get Kubernetes pod logs
def get_pod_logs(pod_name, namespace="default"):
    try:
        v1 = client.CoreV1Api()
        pod_name = pod_name.strip()
        logs = v1.read_namespaced_pod_log(name=pod_name, namespace=namespace)
        return logs
    except client.exceptions.ApiException as e:
        return f"Error: {e.reason}. Details: {e.body}"

# Function to describe a Kubernetes pod
def describe_pod(pod_name, namespace="default"):
    try:
        v1 = client.CoreV1Api()
        pod_name = pod_name.strip()
        pod = v1.read_namespaced_pod(name=pod_name, namespace=namespace)
        return str(pod)
    except client.exceptions.ApiException as e:
        return f"Error: {e.reason}. Details: {e.body}"

# Function to describe a Kubernetes node
def describe_node(node_name):
    try:
        v1 = client.CoreV1Api()
        node_name = node_name.strip()
        node = v1.read_node(name=node_name)
        return str(node)
    except client.exceptions.ApiException as e:
        return f"Error: {e.reason}. Details: {e.body}"
