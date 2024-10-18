# import streamlit as st
# import requests
# from streamlit_lottie import st_lottie
# from PIL import Image
# from streamlit_option_menu import option_menu
# import kubernetes_details  # Import functions from the new file
# import jenkins_status
# from kubernetes_details import load_kubernetes_config, get_pod_logs, describe_pod, describe_node
# import logging
# import login  # Import the login page
# from send_email import send_email  # Import the send_email function
#
#
# # Configure logging
# logging.basicConfig(level=logging.INFO)
#
# # Set page configuration
# st.set_page_config(page_title="DevOps Hub", page_icon=":tada:", layout="wide")
#
# # Check for user authentication (simplified for this example)
# if "authenticated" not in st.session_state:
#     st.session_state.authenticated = False
#
# # Function to load lottie animation from URL
# def load_lottieurl(url):
#     r = requests.get(url)
#     if r.status_code != 200:
#         return None
#     return r.json()
#
# # Function to load local CSS
# def local_css(file_name):
#     with open(file_name) as f:
#         st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
#
# # Load local CSS file
# local_css("style.css")
#
# # Check authentication
# if not st.session_state.authenticated:
#     login.login_page()
# else:
#     # Define menu options
#     selected = option_menu(
#         menu_title=None,
#         options=["Home", "Jenkins", "K8s"],
#         icons=["house", "build", "cloud"],
#         menu_icon="cast",
#         default_index=0,
#         orientation="horizontal",
#         styles={
#             "container": {"padding": "0!important", "background-color": "#f0f0f0"},
#             "icon": {"color": "#0073e6", "font-size": "25px"},
#             "nav-link": {
#                 "font-size": "20px",
#                 "text-align": "center",
#                 "margin": "0px",
#                 "--hover-color": "#d4f1f9"
#             },
#             "nav-link-selected": {"background-color": "#0073e6", "color": "white"},
#         },
#     )
#
#     # Home section
#     if selected == "Home":
#         # Load lottie animation
#         lottie_coding = load_lottieurl("https://lottie.host/0c515a48-108e-46c0-870e-02bb7d022638/qPtkf5RtXn.json")
#
#         # Load images
#         img_contact_form = Image.open("images/images.png")
#         img_lottie_animation = Image.open("images/download.jpg")
#
#         # Header section
#         with st.container():
#             st.subheader("Hi, Welcome :wave:")
#             st.title("DevOps Automation Hub")
#             st.write(
#                 "A DevOps engineer bridges the gap between development and operations, focusing on automating and streamlining processes to improve software delivery."
#             )
#             st.write("[Learn More >](https://pythonandvba.com)")
#
#         # What I do section
#         with st.container():
#             st.write("---")
#             left_column, right_column = st.columns(2)
#             with left_column:
#                 st.header("What I do")
#                 st.write("##")
#                 st.write(
#                     """
#                     - **CI/CD Pipeline Management:** Design, implement, and maintain automated build, test, and deployment pipelines.
#                     - **Infrastructure as Code (IaC):** Use tools like Terraform and Ansible to manage infrastructure through code, ensuring consistency and scalability.
#                     - **Monitoring and Logging:** Implement and maintain monitoring and logging systems to track application performance and troubleshoot issues.
#                     - **Containerization and Orchestration:** Use Docker for containerizing applications and Kubernetes for managing container orchestration.
#                     - **Automation and Scripting:** Automate repetitive tasks and workflows using scripting languages like Bash, Python, or PowerShell.
#                     """
#                 )
#                 st.write("[YouTube Channel >](https://youtube.com/c/CodingIsFun)")
#             with right_column:
#                 st_lottie(lottie_coding, height=400, key="coding")
#
#         # Projects section
#         with st.container():
#             st.write("---")
#             st.header("My Projects")
#             st.write("##")
#             image_column, text_column = st.columns((1, 2))
#             with image_column:
#                 st.image(img_lottie_animation)
#             with text_column:
#                 st.subheader("Integrate Lottie Animations Inside Your Streamlit App")
#                 st.write(
#                     """
#                     Learn how to use Lottie Files in Streamlit! Animations make our web app more engaging and fun, and Lottie Files are the easiest way to do it! In this tutorial, I'll show you exactly how to do it.
#                     """
#                 )
#                 st.markdown("[Watch Video...](https://youtu.be/TXSOitGoINE)")
#
#         with st.container():
#             image_column, text_column = st.columns((1, 2))
#             with image_column:
#                 st.image(img_contact_form)
#             with text_column:
#                 st.subheader("How To Add A Contact Form To Your Streamlit App")
#                 st.write(
#                     """
#                     Want to add a contact form to your Streamlit website? In this video, I'm going to show you how to implement a contact form in your Streamlit app using the free service ‘Form Submit’.
#                     """
#                 )
#                 st.markdown("[Watch Video...](https://youtu.be/FOULV9Xij_8)")
#
#         # Contact section
#         with st.container():
#             st.write("---")
#             st.header("Get In Touch With Me!")
#             st.write("##")
#             contact_form = """
#             <form action="https://formsubmit.co/mannanaxis@gmail.com" method="POST">
#                 <input type="hidden" name="_captcha" value="false">
#                 <input type="text" name="name" placeholder="Your name" required>
#                 <input type="email" name="email" placeholder="Your email" required>
#                 <textarea name="message" placeholder="Your message here" required></textarea>
#                 <button type="submit">Send</button>
#             </form>
#             """
#             left_column, right_column = st.columns(2)
#             with left_column:
#                 st.markdown(contact_form, unsafe_allow_html=True)
#             with right_column:
#                 st.empty()
#
#         # MAIL
#         with st.container():
#             st.write("---")
#             sender_email = st.text_input("Enter your email:")
#             name = st.text_input("Enter your name:")
#             fname = st.text_input("Enter your father's name:")
#             adr = st.text_area("Enter your address:")
#             data = st.selectbox("Enter the domain you're having problem", ('jenkins', 'kubernetes'))
#
#             button = st.button("SUBMIT")
#             if button:
#                 details = f"""
#                     Sender's Email: {sender_email}
#                     Name: {name}
#                     Father's Name: {fname}
#                     Address: {adr}
#                     Problem in: {data}
#                 """
#                 st.markdown(details)
#
#                 # Send email with the form details
#                 subject = "Form Submission"
#                 send_email(sender_email, subject, details)
#
#     # Jenkins section
#     if selected == "Jenkins":
#         st.title(f"You've selected {selected}")
#         jenkins_status.display_pipeline_status()  # Call the function to display Jenkins status
#
#     # Kubernetes section
#     if selected == "K8s":
#         st.title(f"You've selected {selected}")
#
#         # Load Kubernetes configuration
#         load_kubernetes_config()
#
#         # Dropdown menu to select action
#         selected_action = st.selectbox("Select Action",
#                                        [ "Get Pod Logs", "Describe Pod", "Describe Node"])
#
#         # Default namespace
#         namespace = "default"
#
#         # Handle actions based on selection
#         if selected_action == "Get Pod Logs":
#             st.subheader("Pod Logs")
#             pod_name_input = st.text_input("Enter Pod Name:")
#             if st.button("Get Logs"):
#                 if pod_name_input:
#                     pod_logs = get_pod_logs(pod_name_input, namespace=namespace)
#                     if pod_logs.startswith("Error:"):
#                         st.error(pod_logs)
#                     else:
#                         st.code(pod_logs)
#                 else:
#                     st.warning("Please enter a Pod name.")
#
#         elif selected_action == "Describe Pod":
#             st.subheader("Describe Pod")
#             pod_name_desc = st.text_input("Enter Pod Name:")
#             if st.button("Describe Pod"):
#                 if pod_name_desc:
#                     pod_description = describe_pod(pod_name_desc, namespace=namespace)
#                     if pod_description.startswith("Error:"):
#                         st.error(pod_description)
#                     else:
#                         st.code(pod_description)
#                 else:
#                     st.warning("Please enter a Pod name.")
#
#         elif selected_action == "Describe Node":
#             st.subheader("Describe Node")
#             node_name = st.text_input("Enter Node Name:")
#             if st.button("Describe Node"):
#                 if node_name:
#                     node_description = describe_node(node_name)
#                     if node_description.startswith("Error:"):
#                         st.error(node_description)
#                     else:
#                         st.code(node_description)
#                 else:
#                     st.warning("Please enter a Node name.")
#         # Kubernetes details
#
#         # st.subheader("Pod Logs")
#         # pod_name_input = st.text_input("Enter Pod Name:")
#         # if st.button("Get Pod Logs"):
#         #     if pod_name_input:
#         #         pod_logs = get_pod_logs(pod_name_input)
#         #         if pod_logs.startswith("Error:"):
#         #             st.error(pod_logs)
#         #         else:
#         #             st.code(pod_logs)
#         #     else:
#         #         st.warning("Please enter a Pod name.")
#         #
#         # # Describe Pod
#         # st.subheader("Describe Pod")
#         # pod_name_desc = st.text_input("Enter Pod Name:", key="pod_name_desc_input")
#         # if st.button("Describe Pod"):
#         #     if pod_name_desc:
#         #         pod_description = describe_pod(pod_name_desc)
#         #         if pod_description.startswith("Error:"):
#         #             st.error(pod_description)
#         #         else:
#         #             st.code(pod_description)
#         #     else:
#         #         st.warning("Please enter a Pod name.")
#         #
#         # # Describe Node
#         # st.subheader("Describe Node")
#         # node_name = st.text_input("Enter Node Name:", key="node_name_input")
#         # if st.button("Describe Node"):
#         #     if node_name:
#         #         node_description = describe_node(node_name)
#         #         if node_description.startswith("Error:"):
#         #             st.error(node_description)
#         #         else:
#         #             st.code(node_description)
#         #     else:
#         #         st.warning("Please enter a Node name.")
#
#     # if selected == "K8s":
#     #     st.title(f"You've selected {selected}")
#     #
#     #     # Kubernetes details
#     #     st.header("Kubernetes Details")
#     #     option = st.selectbox("Select an option", ["Get Pod Logs", "Describe Pod", "Describe Node"])
#     #
#     #     namespace = st.text_input("Enter Namespace", value="default")
#     #
#     #     if option == "Get Pod Logs":
#     #         pod_name = st.text_input("Enter Pod Name")
#     #         if st.button("Get Logs"):
#     #             if pod_name:
#     #                 with st.spinner('Fetching logs...'):
#     #                     logs = kubernetes_details.get_pod_logs(pod_name, namespace)
#     #                 st.text_area("Logs", logs, height=300)
#     #             else:
#     #                 st.error("Please enter a pod name")
#     #
#     #     elif option == "Describe Pod":
#     #         pod_name = st.text_input("Enter Pod Name")
#     #         if st.button("Describe Pod"):
#     #             if pod_name:
#     #                 with st.spinner('Fetching pod description...'):
#     #                     description = kubernetes_details.describe_pod(pod_name, namespace)
#     #                 st.text_area("Pod Description", description, height=300)
#     #             else:
#     #                 st.error("Please enter a pod name")
#     #
#     #     elif option == "Describe Node":
#     #         node_name = st.text_input("Enter Node Name")
#     #         if st.button("Describe Node"):
#     #             if node_name:
#     #                 with st.spinner('Fetching node description...'):
#     #                     description = kubernetes_details.describe_node(node_name)
#     #                 st.text_area("Node Description", description, height=300)
#     #             else:
#     #                 st.error("Please enter a node name")
#
#     # #MAIL
#     # with st.container():
#     #     st.write("---")
#     #     sender_email = st.text_input("Enter your email:")
#     #     name = st.text_input("Enter your name:")
#     #     fname = st.text_input("Enter your father's name:")
#     #     adr = st.text_area("Enter your address:")
#     #     data = st.selectbox("Enter the domain you're having problem", ('jenkins', 'kubernetes'))
#     #
#     #     button = st.button("Done")
#     #     if button:
#     #         details = f"""
#     #             Sender's Email: {sender_email}
#     #             Name: {name}
#     #             Father's Name: {fname}
#     #             Address: {adr}
#     #             Problem in: {data}
#     #         """
#     #         st.markdown(details)
#     #
#     #         # Send email with the form details
#     #         subject = "Form Submission"
#     #         send_email(sender_email, subject, details)
#
#     # Footer
#     with st.container():
#         st.write("---")
#         st.write("© 2024 DevOps Hub. All rights reserved.")
#
#
#
#
#
#
#
#
#
# #
# # import streamlit as st
# # import requests
# # from streamlit_lottie import st_lottie
# # from PIL import Image
# # from streamlit_option_menu import option_menu
# # import kubernetes_details
# # import jenkins_status
# # from kubernetes_details import load_kubernetes_config, get_pod_logs, describe_pod, describe_node
# # # from app_log import logger  # Import the logger
# # import login
# # from send_email import send_email
# #
# # # Set page configuration
# # st.set_page_config(page_title="DevOps Hub", page_icon=":tada:", layout="wide")
# #
# # logger.info("Streamlit app started")
# #
# # # Check for user authentication (simplified for this example)
# # if "authenticated" not in st.session_state:
# #     st.session_state.authenticated = False
# #     logger.info("User not authenticated")
# #
# # # Function to load lottie animation from URL
# # def load_lottieurl(url):
# #     try:
# #         r = requests.get(url)
# #         r.raise_for_status()
# #         return r.json()
# #     except requests.RequestException as e:
# #         logger.error(f"Error loading Lottie animation: {e}")
# #         return None
# #
# # # Function to load local CSS
# # def local_css(file_name):
# #     try:
# #         with open(file_name) as f:
# #             st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
# #     except FileNotFoundError as e:
# #         logger.error(f"CSS file not found: {e}")
# #
# # # Load local CSS file
# # local_css("style.css")
# #
# # # Check authentication
# # if not st.session_state.authenticated:
# #     login.login_page()
# # else:
# #     # Define menu options
# #     selected = option_menu(
# #         menu_title=None,
# #         options=["Home", "Jenkins", "K8s"],
# #         icons=["house", "build", "cloud"],
# #         menu_icon="cast",
# #         default_index=0,
# #         orientation="horizontal",
# #         styles={
# #             "container": {"padding": "0!important", "background-color": "#f0f0f0"},
# #             "icon": {"color": "#0073e6", "font-size": "25px"},
# #             "nav-link": {
# #                 "font-size": "20px",
# #                 "text-align": "center",
# #                 "margin": "0px",
# #                 "--hover-color": "#d4f1f9"
# #             },
# #             "nav-link-selected": {"background-color": "#0073e6", "color": "white"},
# #         },
# #     )
# #
# #     # Home section
# #     if selected == "Home":
# #         logger.info("Home section selected")
# #
# #         # Load lottie animation
# #         lottie_coding = load_lottieurl("https://lottie.host/0c515a48-108e-46c0-870e-02bb7d022638/qPtkf5RtXn.json")
# #
# #         # Load images
# #         img_contact_form = Image.open("images/images.png")
# #         img_lottie_animation = Image.open("images/download.jpg")
# #
# #         # Header section
# #         with st.container():
# #             st.subheader("Hi, Welcome :wave:")
# #             st.title("DevOps Automation Hub")
# #             st.write(
# #                 "A DevOps engineer bridges the gap between development and operations, focusing on automating and streamlining processes to improve software delivery."
# #             )
# #             st.write("[Learn More >](https://pythonandvba.com)")
# #
# #         # What I do section
# #         with st.container():
# #             st.write("---")
# #             left_column, right_column = st.columns(2)
# #             with left_column:
# #                 st.header("What I do")
# #                 st.write("##")
# #                 st.write(
# #                     """
# #                     - **CI/CD Pipeline Management:** Design, implement, and maintain automated build, test, and deployment pipelines.
# #                     - **Infrastructure as Code (IaC):** Use tools like Terraform and Ansible to manage infrastructure through code, ensuring consistency and scalability.
# #                     - **Monitoring and Logging:** Implement and maintain monitoring and logging systems to track application performance and troubleshoot issues.
# #                     - **Containerization and Orchestration:** Use Docker for containerizing applications and Kubernetes for managing container orchestration.
# #                     - **Automation and Scripting:** Automate repetitive tasks and workflows using scripting languages like Bash, Python, or PowerShell.
# #                     """
# #                 )
# #                 st.write("[YouTube Channel >](https://youtube.com/c/CodingIsFun)")
# #             with right_column:
# #                 st_lottie(lottie_coding, height=400, key="coding")
# #
# #         # Projects section
# #         with st.container():
# #             st.write("---")
# #             st.header("My Projects")
# #             st.write("##")
# #             image_column, text_column = st.columns((1, 2))
# #             with image_column:
# #                 st.image(img_lottie_animation)
# #             with text_column:
# #                 st.subheader("Integrate Lottie Animations Inside Your Streamlit App")
# #                 st.write(
# #                     """
# #                     Learn how to use Lottie Files in Streamlit! Animations make our web app more engaging and fun, and Lottie Files are the easiest way to do it! In this tutorial, I'll show you exactly how to do it.
# #                     """
# #                 )
# #                 st.markdown("[Watch Video...](https://youtu.be/TXSOitGoINE)")
# #
# #         with st.container():
# #             image_column, text_column = st.columns((1, 2))
# #             with image_column:
# #                 st.image(img_contact_form)
# #             with text_column:
# #                 st.subheader("How To Add A Contact Form To Your Streamlit App")
# #                 st.write(
# #                     """
# #                     Want to add a contact form to your Streamlit website? In this video, I'm going to show you how to implement a contact form in your Streamlit app using the free service ‘Form Submit’.
# #                     """
# #                 )
# #                 st.markdown("[Watch Video...](https://youtu.be/FOULV9Xij_8)")
# #
# #         # Contact section
# #         with st.container():
# #             st.write("---")
# #             st.header("Get In Touch With Me!")
# #             st.write("##")
# #             contact_form = """
# #             <form action="https://formsubmit.co/mannanaxis@gmail.com" method="POST">
# #                 <input type="hidden" name="_captcha" value="false">
# #                 <input type="text" name="name" placeholder="Your name" required>
# #                 <input type="email" name="email" placeholder="Your email" required>
# #                 <textarea name="message" placeholder="Your message here" required></textarea>
# #                 <button type="submit">Send</button>
# #             </form>
# #             """
# #             left_column, right_column = st.columns(2)
# #             with left_column:
# #                 st.markdown(contact_form, unsafe_allow_html=True)
# #             with right_column:
# #                 st.empty()
# #
# #         # MAIL
# #         with st.container():
# #             st.write("---")
# #             sender_email = st.text_input("Enter your email:")
# #             name = st.text_input("Enter your name:")
# #             fname = st.text_input("Enter your father's name:")
# #             adr = st.text_area("Enter your address:")
# #             data = st.selectbox("Enter the domain you're having problem", ('jenkins', 'kubernetes'))
# #
# #             button = st.button("SUBMIT")
# #             if button:
# #                 details = f"""
# #                     Sender's Email: {sender_email}
# #                     Name: {name}
# #                     Father's Name: {fname}
# #                     Address: {adr}
# #                     Problem in: {data}
# #                 """
# #                 st.markdown(details)
# #
# #                 # Send email with the form details
# #                 subject = "Form Submission"
# #                 send_email(sender_email, subject, details)
# #                 logger.info(f"Email sent: {details}")
# #
# #     # Jenkins section
# #     if selected == "Jenkins":
# #         st.title(f"You've selected {selected}")
# #         logger.info("Jenkins section selected")
# #         jenkins_status.display_pipeline_status()  # Call the function to display Jenkins status
# #
# #     # Kubernetes section
# #     if selected == "K8s":
# #         st.title(f"You've selected {selected}")
# #
# #         # Load Kubernetes configuration
# #         load_kubernetes_config()
# #         logger.info("Kubernetes configuration loaded")
# #
# #         # Dropdown menu to select action
# #         selected_action = st.selectbox("Select Action",
# #                                        [ "Get Pod Logs", "Describe Pod", "Describe Node"])
# #
# #         # Default namespace
# #         namespace = "default"
# #
# #         # Handle actions based on selection
# #         if selected_action == "Get Pod Logs":
# #             st.subheader("Pod Logs")
# #             pod_name_input = st.text_input("Enter Pod Name:")
# #             if st.button("Get Logs"):
# #                 if pod_name_input:
# #                     pod_logs = get_pod_logs(pod_name_input, namespace=namespace)
# #                     if pod_logs.startswith("Error:"):
# #                         st.error(pod_logs)
# #                         logger.error(f"Error getting pod logs: {pod_logs}")
# #                     else:
# #                         st.code(pod_logs)
# #                         logger.info(f"Pod logs retrieved for pod: {pod_name_input}")
# #                 else:
# #                     st.warning("Please enter a Pod name.")
# #                     logger.warning("No Pod name provided")
# #
# #         elif selected_action == "Describe Pod":
# #             st.subheader("Describe Pod")
# #             pod_name_desc = st.text_input("Enter Pod Name:")
# #             if st.button("Describe Pod"):
# #                 if pod_name_desc:
# #                     pod_description = describe_pod(pod_name_desc, namespace=namespace)
# #                     if pod_description.startswith("Error:"):
# #                         st.error(pod_description)
# #                         logger.error(f"Error describing pod: {pod_description}")
# #                     else:
# #                         st.code(pod_description)
# #                         logger.info(f"Pod description retrieved for pod: {pod_name_desc}")
# #                 else:
# #                     st.warning("Please enter a Pod name.")
# #                     logger.warning("No Pod name provided")
# #
# #         elif selected_action == "Describe Node":
# #             st.subheader("Describe Node")
# #             node_name = st.text_input("Enter Node Name:")
# #             if st.button("Describe Node"):
# #                 if node_name:
# #                     node_description = describe_node(node_name)
# #                     if node_description.startswith("Error:"):
# #                         st.error(node_description)
# #                         logger.error(f"Error describing node: {node_description}")
# #                     else:
# #                         st.code(node_description)
# #                         logger.info(f"Node description retrieved for node: {node_name}")
# #                 else:
# #                     st.warning("Please enter a Node name.")
# #                     logger.warning("No Node name provided")
# #
# #     # Footer
# #     with st.container():
# #         st.write("---")
# #         st.write("© 2024 DevOps Hub. All rights reserved.")
# #         logger.info("Footer displayed")





import streamlit as st
import requests
from streamlit_lottie import st_lottie
from PIL import Image
from streamlit_option_menu import option_menu
import kubernetes_details  # Import functions from the new file
import jenkins_status
from kubernetes_details import (load_kubernetes_config, get_pod_logs, describe_pod, describe_node)
import logging
import login  # Import the login page
from send_email import send_email  # Import the send_email function
from ELK.logConfig import setup_logging
from Minikube import minikube_status, start_minikube, stop_minikube, minikube_info

# Set up logging
setup_logging()

# Configure logging
logging.basicConfig(filename='app.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Set page configuration
st.set_page_config(page_title="DevOps Hub", page_icon=":tada:", layout="wide")
logging.info("Streamlit app configuration set.")

# Check for user authentication (simplified for this example)
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False
    logging.info("Session state initialized with 'authenticated' set to False.")

# Function to load lottie animation from URL
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        logging.error(f"Failed to load Lottie animation from {url}")
        return None
    logging.info(f"Lottie animation loaded successfully from {url}")
    return r.json()

# Function to load local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
        logging.info(f"Local CSS file {file_name} loaded.")

# Load local CSS file
local_css("style.css")

# Check authentication
if not st.session_state.authenticated:
    logging.info("User not authenticated. Displaying login page.")
    login.login_page()
else:
    # Define menu options
    selected = option_menu(
        menu_title=None,
        options=["Home", "Jenkins", "K8s", "Minikube"],
        icons=["house", "build", "cloud", "server"],
        menu_icon="cast",
        default_index=0,
        orientation="horizontal",
        styles={
            "container": {"padding": "0!important", "background-color": "#f0f0f0"},
            "icon": {"color": "#0073e6", "font-size": "25px"},
            "nav-link": {
                "font-size": "20px",
                "text-align": "center",
                "margin": "0px",
                "--hover-color": "#d4f1f9"
            },
            "nav-link-selected": {"background-color": "#0073e6", "color": "white"},
        },
    )
    logging.info(f"User selected menu option: {selected}")

    # Home section
    if selected == "Home":
        logging.info("Displaying Home section.")
        # Load lottie animation
        lottie_coding = load_lottieurl("https://lottie.host/0c515a48-108e-46c0-870e-02bb7d022638/qPtkf5RtXn.json")

        # Load images
        img_contact_form = Image.open("images/images.png")
        img_lottie_animation = Image.open("images/download.jpg")

        # Header section
        with st.container():
            st.subheader("Hi, Welcome :wave:")
            st.title("DevOps Automation Hub")
            st.write(
                "A DevOps engineer bridges the gap between development and operations, focusing on automating and streamlining processes to improve software delivery."
            )
            st.write("[Learn More >](https://pythonandvba.com)")

        # What I do section
        with st.container():
            st.write("---")
            left_column, right_column = st.columns(2)
            with left_column:
                st.header("What I do")
                st.write("##")
                st.write(
                    """
                    - **CI/CD Pipeline Management:** Design, implement, and maintain automated build, test, and deployment pipelines.
                    - **Infrastructure as Code (IaC):** Use tools like Terraform and Ansible to manage infrastructure through code, ensuring consistency and scalability.
                    - **Monitoring and Logging:** Implement and maintain monitoring and logging systems to track application performance and troubleshoot issues.
                    - **Containerization and Orchestration:** Use Docker for containerizing applications and Kubernetes for managing container orchestration.
                    - **Automation and Scripting:** Automate repetitive tasks and workflows using scripting languages like Bash, Python, or PowerShell.
                    """
                )
                st.write("[YouTube Channel >](https://youtube.com/c/CodingIsFun)")
            with right_column:
                st_lottie(lottie_coding, height=400, key="coding")

        # Projects section
        with st.container():
            st.write("---")
            st.header("My Projects")
            st.write("##")
            image_column, text_column = st.columns((1, 2))
            with image_column:
                st.image(img_lottie_animation)
            with text_column:
                st.subheader("Integrate Lottie Animations Inside Your Streamlit App")
                st.write(
                    """
                    Learn how to use Lottie Files in Streamlit! Animations make our web app more engaging and fun, and Lottie Files are the easiest way to do it! In this tutorial, I'll show you exactly how to do it.
                    """
                )
                st.markdown("[Watch Video...](https://youtu.be/TXSOitGoINE)")

        with st.container():
            image_column, text_column = st.columns((1, 2))
            with image_column:
                st.image(img_contact_form)
            with text_column:
                st.subheader("How To Add A Contact Form To Your Streamlit App")
                st.write(
                    """
                    Want to add a contact form to your Streamlit website? In this video, I'm going to show you how to implement a contact form in your Streamlit app using the free service ‘Form Submit’.
                    """
                )
                st.markdown("[Watch Video...](https://youtu.be/FOULV9Xij_8)")

        # Contact section
        with st.container():
            st.write("---")
            st.header("Get In Touch With Me!")
            st.write("##")
            contact_form = """
            <form action="https://formsubmit.co/mannanaxis@gmail.com" method="POST">
                <input type="hidden" name="_captcha" value="false">
                <input type="text" name="name" placeholder="Your name" required>
                <input type="email" name="email" placeholder="Your email" required>
                <textarea name="message" placeholder="Your message here" required></textarea>
                <button type="submit">Send</button>
            </form>
            """
            left_column, right_column = st.columns(2)
            with left_column:
                st.markdown(contact_form, unsafe_allow_html=True)
            with right_column:
                st.empty()

        # MAIL
        with st.container():
            st.write("---")
            sender_email = st.text_input("Enter your email:")
            name = st.text_input("Enter your name:")
            fname = st.text_input("Enter your father's name:")
            adr = st.text_area("Enter your address:")
            data = st.selectbox("Enter the domain you're having problem", ('jenkins', 'kubernetes'))

            button = st.button("SUBMIT")
            if button:
                details = f"""
                    Sender's Email: {sender_email}
                    Name: {name}
                    Father's Name: {fname}
                    Address: {adr}
                    Problem in: {data}
                """
                st.markdown(details)

                # Send email with the form details
                subject = "Form Submission"
                send_email(sender_email, subject, details)
                logging.info("Contact form submitted. Details: %s", details)

    # Jenkins section
    if selected == "Jenkins":
        logging.info("Displaying Jenkins section.")
        st.title(f"You've selected {selected}")
        jenkins_status.display_pipeline_status()  # Call the function to display Jenkins status

    # Kubernetes section
    if selected == "K8s":
        logging.info("Displaying Kubernetes section.")
        st.title(f"You've selected {selected}")

        # Load Kubernetes configuration
        load_kubernetes_config()

        # Dropdown menu to select action
        selected_action = st.selectbox("Select Action",
                                       [ "Get Pod Logs", "Describe Pod", "Describe Node"])

        # Default namespace
        namespace = "default"

        # Handle actions based on selection
        if selected_action == "Get Pod Logs":
            logging.info("Selected 'Get Pod Logs' action.")
            st.subheader("Pod Logs")
            pod_name_input = st.text_input("Enter Pod Name:")
            if st.button("Get Logs"):
                if pod_name_input:
                    pod_logs = get_pod_logs(pod_name_input, namespace=namespace)
                    if pod_logs.startswith("Error:"):
                        st.error(pod_logs)
                        logging.error("Error fetching pod logs for pod: %s", pod_name_input)
                    else:
                        st.code(pod_logs)
                        logging.info("Fetched pod logs for pod: %s", pod_name_input)
                else:
                    st.warning("Please enter a Pod name.")
                    logging.warning("Pod name input is empty.")

        elif selected_action == "Describe Pod":
            logging.info("Selected 'Describe Pod' action.")
            st.subheader("Describe Pod")
            pod_name_desc = st.text_input("Enter Pod Name:")
            if st.button("Describe Pod"):
                if pod_name_desc:
                    pod_description = describe_pod(pod_name_desc, namespace=namespace)
                    if pod_description.startswith("Error:"):
                        st.error(pod_description)
                        logging.error("Error describing pod: %s", pod_name_desc)
                    else:
                        st.code(pod_description)
                        logging.info("Described pod: %s", pod_name_desc)
                else:
                    st.warning("Please enter a Pod name.")
                    logging.warning("Pod name input is empty.")

        elif selected_action == "Describe Node":
            logging.info("Selected 'Describe Node' action.")
            st.subheader("Describe Node")
            node_name_input = st.text_input("Enter Node Name:")
            if st.button("Describe Node"):
                if node_name_input:
                    node_description = describe_node(node_name_input)
                    if node_description.startswith("Error:"):
                        st.error(node_description)
                        logging.error("Error describing node: %s", node_name_input)
                    else:
                        st.code(node_description)
                        logging.info("Described node: %s", node_name_input)
                else:
                    st.warning("Please enter a Node name.")
                    logging.warning("Node name input is empty.")

    # Minikube section
    if selected == "Minikube":
        logging.info("Displaying Minikube section.")
        st.title(f"You've selected {selected}")

        # Show Minikube Status
        with st.container():
            st.subheader("Minikube Status")
            minikube_status_output = minikube_status()
            st.code(minikube_status_output)

        # Buttons to start or stop Minikube
        with st.container():
            st.write("---")
            if st.button("Start Minikube"):
                output = start_minikube()
                st.code(output)

            if st.button("Stop Minikube"):
                output = stop_minikube()
                st.code(output)

        # Show Minikube cluster info
        with st.container():
            st.write("---")
            st.subheader("Minikube Cluster Info")
            if st.button("Get Cluster Info"):
                cluster_info = minikube_info()
                st.code(cluster_info)






