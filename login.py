import streamlit as st
from streamlit_lottie import st_lottie
import requests
from header import header
from RBAC.user import register_user, authenticate_user


def login_page():
    # Header
    st.markdown(header(), unsafe_allow_html=True)

    # Load Lottie animation
    def load_lottieurl(url):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()

    # Import CSS file for styling
    st.markdown(
        '<link rel="stylesheet" type="text/css" href="./style/login.css">',
        unsafe_allow_html=True
    )

    st.markdown('<div class="login-container">', unsafe_allow_html=True)

    st.markdown('<h2 class="login-title">Login</h2>', unsafe_allow_html=True)

    lottie_coding = load_lottieurl("https://lottie.host/19375b79-c9bf-4afc-a80f-e0124bf214da/yXR9TVbtZN.json")

    with st.container():
        st.write("---")
        left_column, right_column = st.columns(2)

        # Show login form if user is not in register mode
        if "register_mode" not in st.session_state or not st.session_state["register_mode"]:
            with left_column:
                id = st.text_input("ID", key="login-id-input")
                password = st.text_input("Password", type="password", key="login-password-input")
                if st.button("Login", key="login-button"):
                    # Hardcoded credentials check for 'devops'
                    if id == "devops" and password == "devops":
                        st.success("Login successful")
                        st.session_state.authenticated = True
                        st.experimental_rerun()  # This will rerun the app to reflect the change in session state
                    else:
                        # Authenticate using plaintext password
                        user = authenticate_user(id, password)
                        if user:
                            st.success(f"Welcome, {user['username']}!")
                            st.session_state.authenticated = True
                            st.experimental_rerun()  # This will rerun the app to reflect the change in session state
                        else:
                            st.markdown('<p class="login-error">Incorrect ID or Password</p>', unsafe_allow_html=True)

                if st.button("Register as a new user"):
                    # Switch to the registration mode
                    st.session_state["register_mode"] = True
                    st.experimental_rerun()  # Rerun to refresh the page to show registration form

        # Show register form when in register_mode
        if "register_mode" in st.session_state and st.session_state["register_mode"]:
            register_page()

        with right_column:
            st_lottie(lottie_coding, height=400, key="coding")

    st.markdown('</div>', unsafe_allow_html=True)


def register_page():
    st.title("Register")

    # Display the registration form
    username = st.text_input("Username", key="register-username-input")
    password = st.text_input("Password", type="password", key="register-password-input")
    role = st.selectbox("Role", ["admin", "user", "guest"], key="register-role")

    if st.button("Register", key="register-button"):
        # Register user with plaintext password
        result = register_user(username, password, role)
        if result:
            st.success("Registration successful! You can now log in.")
            st.session_state["register_mode"] = False  # Switch back to login mode
            st.experimental_rerun()  # Refresh the page to show the login form
        else:
            st.error("Registration failed. Please try again.")
            st.session_state["register_mode"] = False  # Switch back to login mode















# import streamlit as st
# from streamlit_lottie import st_lottie
# import requests
# from header import header
# from RBAC.user import register_user, authenticate_user
# import hashlib
#
#
# def login_page():
#     # Header
#     st.markdown(header(), unsafe_allow_html=True)
#
#     # Load Lottie animation
#     def load_lottieurl(url):
#         r = requests.get(url)
#         if r.status_code != 200:
#             return None
#         return r.json()
#
#     # Import CSS file for styling
#     st.markdown(
#         '<link rel="stylesheet" type="text/css" href="./style/login.css">',
#         unsafe_allow_html=True
#     )
#
#     st.markdown('<div class="login-container">', unsafe_allow_html=True)
#
#     st.markdown('<h2 class="login-title">Login</h2>', unsafe_allow_html=True)
#
#     lottie_coding = load_lottieurl("https://lottie.host/19375b79-c9bf-4afc-a80f-e0124bf214da/yXR9TVbtZN.json")
#
#     with st.container():
#         st.write("---")
#         left_column, right_column = st.columns(2)
#
#         # Show login form if user is not in register mode
#         if "register_mode" not in st.session_state or not st.session_state["register_mode"]:
#             with left_column:
#                 id = st.text_input("ID", key="login-id-input")
#                 password = st.text_input("Password", type="password", key="login-password-input")
#                 if st.button("Login", key="login-button"):
#                     # Hardcoded credentials check for 'devops'
#                     if id == "devops" and password == "devops":
#                         st.success("Login successful")
#                         st.session_state.authenticated = True
#                         st.experimental_rerun()  # This will rerun the app to reflect the change in session state
#                     else:
#                         # Use database credentials for authentication
#                         user = authenticate_user(id, password)
#                         if user:
#                             st.success(f"Welcome, {user['username']}!")
#                             st.session_state.authenticated = True
#                             st.experimental_rerun()  # This will rerun the app to reflect the change in session state
#                         else:
#                             st.markdown('<p class="login-error">Incorrect ID or Password</p>', unsafe_allow_html=True)
#
#                 if st.button("Register as a new user"):
#                     # Switch to the registration mode
#                     st.session_state["register_mode"] = True
#                     st.experimental_rerun()  # Rerun to refresh the page to show registration form
#
#         # Show register form when in register_mode
#         if "register_mode" in st.session_state and st.session_state["register_mode"]:
#             register_page()
#
#         with right_column:
#             st_lottie(lottie_coding, height=400, key="coding")
#
#     st.markdown('</div>', unsafe_allow_html=True)
#
#
# def register_page():
#     st.title("Register")
#
#     # Display the registration form
#     username = st.text_input("Username", key="register-username-input")
#     password = st.text_input("Password", type="password", key="register-password-input")
#     role = st.selectbox("Role", ["admin", "user", "guest"], key="register-role")
#
#     if st.button("Register", key="register-button"):
#         # Hash the password before saving to the database
#         hashed_password = hashlib.sha256(password.encode()).hexdigest()
#
#         # Call the register_user function and check if the registration is successful
#         result = register_user(username, hashed_password, role)
#         if result:
#             st.success("Registration successful! You can now log in.")
#             st.session_state["register_mode"] = False  # Switch back to login mode
#             st.experimental_rerun()  # Refresh the page to show the login form
#         else:
#             st.error("Registration failed. Please try again.")
#             st.session_state["register_mode"] = False  # Switch back to login mode
#
#



# import streamlit as st
# from streamlit_lottie import st_lottie
# import requests
# import logging
# from header import header
#
# # Configure logging
# logging.basicConfig(
#     format='%(asctime)s - %(levelname)s - %(message)s',
#     level=logging.INFO
# )
# logger = logging.getLogger()
#
# def login_page():
#     # Header
#     st.markdown(header(), unsafe_allow_html=True)
#
#     # Load Lottie animation
#     def load_lottieurl(url):
#         r = requests.get(url)
#         if r.status_code != 200:
#             logger.error(f"Failed to load Lottie animation from {url} with status code {r.status_code}")
#             return None
#         return r.json()
#
#     # Import CSS file for styling
#     st.markdown(
#         '<link rel="stylesheet" type="text/css" href="./style/login.css">',
#         unsafe_allow_html=True
#     )
#
#     st.markdown('<div class="login-container">', unsafe_allow_html=True)
#
#     st.markdown('<h2 class="login-title">Login</h2>', unsafe_allow_html=True)
#
#     lottie_coding = load_lottieurl("https://lottie.host/19375b79-c9bf-4afc-a80f-e0124bf214da/yXR9TVbtZN.json")
#
#     with st.container():
#         st.write("---")
#         left_column, right_column = st.columns(2)
#         with left_column:
#             id = st.text_input("ID", key="login-id-input")
#             password = st.text_input("Password", type="password", key="login-password-input")
#             if st.button("Login", key="login-button"):
#                 if id == "devops" and password == "devops":
#                     st.success("Login successful")
#                     logger.info(f"User '{id}' logged in successfully.")
#                     st.session_state.authenticated = True
#                     st.experimental_rerun()  # This will rerun the app to reflect the change in session state
#                 else:
#                     st.markdown('<p class="login-error">Incorrect ID or Password</p>', unsafe_allow_html=True)
#                     logger.warning(f"Failed login attempt for user '{id}'.")
#
#         with right_column:
#             st_lottie(lottie_coding, height=400, key="coding")
#
#     st.markdown('</div>', unsafe_allow_html=True)
#
# # Run the login page function
# if __name__ == "__main__":
#     logger.info("Login service started.")
#     login_page()







# --------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------


# import streamlit as st
# from streamlit_lottie import st_lottie
# import requests
# from header import header
#
# def login_page():
#     # Header
#     st.markdown(header(), unsafe_allow_html=True)
#
#     # Load Lottie animation
#     def load_lottieurl(url):
#         r = requests.get(url)
#         if r.status_code != 200:
#             return None
#         return r.json()
#
#     # Import CSS file for styling
#     st.markdown(
#         '<link rel="stylesheet" type="text/css" href="./style/login.css">',
#         unsafe_allow_html=True
#     )
#
#     st.markdown('<div class="login-container">', unsafe_allow_html=True)
#
#     st.markdown('<h2 class="login-title">Login</h2>', unsafe_allow_html=True)
#
#     lottie_coding = load_lottieurl("https://lottie.host/19375b79-c9bf-4afc-a80f-e0124bf214da/yXR9TVbtZN.json")
#
#     with st.container():
#         st.write("---")
#         left_column, right_column = st.columns(2)
#         with left_column:
#             id = st.text_input("ID", key="login-id-input")
#             password = st.text_input("Password", type="password", key="login-password-input")
#             if st.button("Login", key="login-button"):
#                 if id == "devops" and password == "devops":
#                     st.success("Login successful")
#                     st.session_state.authenticated = True
#                     st.experimental_rerun()  # This will rerun the app to reflect the change in session state
#                 else:
#                     st.markdown('<p class="login-error">Incorrect ID or Password</p>', unsafe_allow_html=True)
#
#         with right_column:
#             st_lottie(lottie_coding, height=400, key="coding")
#
#     st.markdown('</div>', unsafe_allow_html=True)
#
# login_page()




#
# import streamlit as st
# from streamlit_lottie import st_lottie
# import requests
# import logging
# from header import header
#
# # Assuming logging is configured in a separate file (app_log.py)
# from LOGS.app_log  import setup_logging
#
# # Call the logging setup function to configure logging
# setup_logging()
#
# def login_page():
#     # Header (Assuming header() is defined elsewhere)
#     st.markdown(header(), unsafe_allow_html=True)
#
#     # Load Lottie animation
#     def load_lottieurl(url):
#         r = requests.get(url)
#         if r.status_code != 200:
#             return None
#         return r.json()
#
#     # Import CSS file for styling
#     st.markdown(
#         '<link rel="stylesheet" type="text/css" href="./style/login.css">',
#         unsafe_allow_html=True
#     )
#
#     st.markdown('<div class="login-container">', unsafe_allow_html=True)
#     st.markdown('<h2 class="login-title">Login</h2>', unsafe_allow_html=True)
#
#     lottie_coding = load_lottieurl("https://lottie.host/19375b79-c9bf-4afc-a80f-e0124bf214da/yXR9TVbtZN.json")
#
#     with st.container():
#         st.write("---")
#         left_column, right_column = st.columns(2)
#         with left_column:
#             id = st.text_input("ID", key="login-id-input")
#             password = st.text_input("Password", type="password", key="login-password-input")
#
#             # Handle the login button
#             if st.button("Login", key="login-button"):
#                 # Log the login attempt
#                 logging.info(f"Login attempt by user: {id}")
#
#                 if id == "devops" and password == "devops":
#                     st.success("Login successful")
#                     logging.info(f"Login successful for user: {id}")  # Log successful login
#                     st.session_state.authenticated = True
#                     st.experimental_rerun()  # Rerun to update session state
#                 else:
#                     st.markdown('<p class="login-error">Incorrect ID or Password</p>', unsafe_allow_html=True)
#                     logging.warning(f"Login failed for user: {id}")  # Log failed login
#
#         with right_column:
#             st_lottie(lottie_coding, height=400, key="coding")
#
#     st.markdown('</div>', unsafe_allow_html=True)
#
# # Call the login page function
# login_page()
