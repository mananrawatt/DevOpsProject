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
                    if id == "devops" and password == "devops":
                        st.success("Login successful")
                        st.session_state.authenticated = True
                        st.session_state["current_page"] = "dashboard"  # Set the page to 'dashboard'
                        st.experimental_rerun()  # Rerun to reflect the change in session state
                    else:
                        user = authenticate_user(id, password)
                        if user:
                            st.success(f"Welcome, {user['username']}!")
                            st.session_state.authenticated = True
                            st.session_state["current_page"] = "dashboard"  # Redirect to dashboard
                            st.experimental_rerun()  # Refresh to show dashboard
                        else:
                            st.markdown('<p class="login-error">Incorrect ID or Password</p>', unsafe_allow_html=True)

                if st.button("Register as a new user"):
                    # Switch to the registration mode
                    st.session_state["register_mode"] = True
                    st.experimental_rerun()  # Rerun to show the registration form

        if "current_page" in st.session_state and st.session_state["current_page"] == "dashboard":
            dashboard_page()  # Redirect to the dashboard after login

        # Show register form when in register_mode
        if "register_mode" in st.session_state and st.session_state["register_mode"]:
            register_page()

        with right_column:
            st_lottie(lottie_coding, height=400, key="coding")

    st.markdown('</div>', unsafe_allow_html=True)


def register_page():
    st.title("Register")

    username = st.text_input("Username", key="register-username-input")
    password = st.text_input("Password", type="password", key="register-password-input")
    role = st.selectbox("Role", ["admin", "user", "guest"], key="register-role")

    if st.button("Register", key="register-button"):
        result = register_user(username, password, role)
        if result:
            st.success("Registration successful! You can now log in.")
            st.session_state["register_mode"] = False
            st.session_state["current_page"] = "login"  # Switch to login page
            st.experimental_rerun()  # Rerun to show login page
        else:
            st.error("Registration failed. Please try again.")

def dashboard_page():
    st.title("Dashboard")
    # Your dashboard content goes here

    if st.button("Logout"):
        st.session_state["authenticated"] = False
        st.session_state["current_page"] = "login"  # Redirect to login
        st.experimental_rerun()  # Refresh to show login page















# import streamlit as st
# from streamlit_lottie import st_lottie
# import requests
# from header import header
# from RBAC.user import register_user, authenticate_user
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
#                         # Authenticate using plaintext password
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
#         # Register user with plaintext password
#         result = register_user(username, password, role)
#         if result:
#             st.success("Registration successful! You can now log in.")
#             st.session_state["register_mode"] = False  # Switch back to login mode
#             st.experimental_rerun()  # Refresh the page to show the login form
#         else:
#             st.error("Registration failed. Please try again.")
#             st.session_state["register_mode"] = False  # Switch back to login mode
#
#
#
#
#
#
#
#
#
#
#
#
#
#
