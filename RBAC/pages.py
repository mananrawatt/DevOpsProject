# pages.py

import streamlit as st
from .user import register_user, authenticate_user

# Registration Page
def register_page():
    st.title("Register")
    username = st.text_input("Username", key="register_username")
    password = st.text_input("Password", type="password", key="register_password")
    role = st.selectbox("Role", ["admin", "user", "guest"], key="register_role")

    if st.button("Register", key="register_button"):
        register_user(username, password, role)

# Login Page
def login_page():
    st.title("Login")
    username = st.text_input("Username", key="login_username")
    password = st.text_input("Password", type="password", key="login_password")

    if st.button("Login", key="login_button"):
        user = authenticate_user(username, password)
        if user:
            st.session_state["username"] = user["username"]
            st.session_state["role"] = user["role"]
            st.success(f"Welcome, {user['username']}! You are logged in as {user['role']}.")
        else:
            st.error("Invalid username or password")
    if st.button("Register", key="register_button_in_login"):
        register_page()

# Main Dashboard Page
def main_page():
    if "role" in st.session_state:
        st.title("Dashboard")
        role = st.session_state["role"]
        if role == "admin":
            st.write("Admin Dashboard: Full Access")
        elif role == "user":
            st.write("User Dashboard: Limited Access")
        else:
            st.write("Guest Dashboard: Very Limited Access")
    else:
        login_page()
