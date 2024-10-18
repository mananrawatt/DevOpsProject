import subprocess
import logging

# Function to check Minikube status
def minikube_status():
    try:
        result = subprocess.run(["minikube", "status"], capture_output=True, text=True)
        if result.returncode == 0:
            logging.info("Minikube status fetched successfully.")
            return result.stdout
        else:
            logging.error("Failed to fetch Minikube status.")
            return "Minikube is not running."
    except Exception as e:
        logging.error(f"Error checking Minikube status: {e}")
        return str(e)

# Function to start Minikube
def start_minikube():
    try:
        result = subprocess.run(["minikube", "start"], capture_output=True, text=True)
        if result.returncode == 0:
            logging.info("Minikube started successfully.")
            return "Minikube started successfully."
        else:
            logging.error(f"Failed to start Minikube: {result.stderr}")
            return result.stderr
    except Exception as e:
        logging.error(f"Error starting Minikube: {e}")
        return str(e)

# Function to stop Minikube
def stop_minikube():
    try:
        result = subprocess.run(["minikube", "stop"], capture_output=True, text=True)
        if result.returncode == 0:
            logging.info("Minikube stopped successfully.")
            return "Minikube stopped successfully."
        else:
            logging.error(f"Failed to stop Minikube: {result.stderr}")
            return result.stderr
    except Exception as e:
        logging.error(f"Error stopping Minikube: {e}")
        return str(e)

# Function to get Minikube cluster info
def minikube_info():
    try:
        result = subprocess.run(["kubectl", "get", "all", "--namespace=default"], capture_output=True, text=True)
        if result.returncode == 0:
            logging.info("Fetched Minikube cluster info successfully.")
            return result.stdout
        else:
            logging.error(f"Failed to fetch Minikube info: {result.stderr}")
            return result.stderr
    except Exception as e:
        logging.error(f"Error fetching Minikube cluster info: {e}")
        return str(e)
