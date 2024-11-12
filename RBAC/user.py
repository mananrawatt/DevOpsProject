from .connection import create_connection
import mysql.connector
import streamlit as st


def register_user(username, password, role):
    """Registers a new user in the database without hashing the password."""
    try:
        connection = create_connection()
        if connection:
            cursor = connection.cursor()

            # Check if the username already exists
            cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
            existing_user = cursor.fetchone()
            if existing_user:
                st.error(f"Username '{username}' already exists.")
                return False

            # Insert the new user into the database with plaintext password
            query = "INSERT INTO users (username, password, role) VALUES (%s, %s, %s)"
            cursor.execute(query, (username, password, role))  # Store password as plaintext
            connection.commit()

            # Check if the user was inserted successfully
            if cursor.rowcount > 0:
                return True
            else:
                return False
    except mysql.connector.Error as e:
        st.error(f"Error registering user: {e}")
        return False
    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()


def authenticate_user(username, password):
    """Authenticates a user based on username and plaintext password."""
    try:
        connection = create_connection()
        if connection:
            cursor = connection.cursor(dictionary=True)
            query = "SELECT * FROM users WHERE username = %s AND password = %s"
            cursor.execute(query, (username, password))  # No hashing, compare plaintext password
            user = cursor.fetchone()

            if user:
                return user  # Authentication successful
            else:
                return None  # Authentication failed
    except mysql.connector.Error as e:
        st.error(f"Error during authentication: {e}")
        return None
    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()








# from .connection import create_connection
# import mysql.connector
# import streamlit as st
# import hashlib
#
#
# def register_user(username, password, role):
#     """Registers a new user in the database."""
#     try:
#         # Hash the password before storing it
#         hashed_password = hashlib.sha256(password.encode()).hexdigest()
#
#         connection = create_connection()
#         if connection:
#             cursor = connection.cursor()
#
#             # Check if the username already exists
#             cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
#             existing_user = cursor.fetchone()
#             if existing_user:
#                 st.error(f"Username '{username}' already exists.")
#                 return False
#
#             # Insert the new user into the database
#             query = "INSERT INTO users (username, password, role) VALUES (%s, %s, %s)"
#             cursor.execute(query, (username, hashed_password, role))
#             connection.commit()
#
#             # Check if the user was inserted successfully
#             if cursor.rowcount > 0:
#                 return True
#             else:
#                 return False
#     except mysql.connector.Error as e:
#         st.error(f"Error registering user: {e}")
#         return False
#     finally:
#         if connection and connection.is_connected():
#             cursor.close()
#             connection.close()
#
#
# def authenticate_user(username, password):
#     """Authenticates a user based on username and password."""
#     try:
#         # Hash the password entered during login
#         hashed_password = hashlib.sha256(password.encode()).hexdigest()
#         print(f"Hashed password: {hashed_password}")  # Debugging line
#
#         connection = create_connection()
#         if connection:
#             cursor = connection.cursor(dictionary=True)
#             query = "SELECT * FROM users WHERE username = %s AND password = %s"
#             cursor.execute(query, (username, hashed_password))
#             user = cursor.fetchone()
#
#             if user:
#                 return user  # Authentication successful
#             else:
#                 return None  # Authentication failed
#     except mysql.connector.Error as e:
#         st.error(f"Error during authentication: {e}")
#         return None
#     finally:
#         if connection and connection.is_connected():
#             cursor.close()
#             connection.close()

# def authenticate_user(username, password):
#     """Authenticates a user based on username and password."""
#     try:
#         # Hash the password before comparing it to the stored one
#         hashed_password = hashlib.sha256(password.encode()).hexdigest()
#
#         connection = create_connection()
#         if connection:
#             cursor = connection.cursor(dictionary=True)
#             query = "SELECT * FROM users WHERE username = %s AND password = %s"
#             cursor.execute(query, (username, hashed_password))
#             user = cursor.fetchone()
#             return user
#     except mysql.connector.Error as e:
#         st.error(f"Error during authentication: {e}")
#         return None
#     finally:
#         if connection and connection.is_connected():
#             cursor.close()
#             connection.close()
#
#
#
#
#

# # user_management.py
#
# from .connection import create_connection
# import mysql.connector
# import streamlit as st
#
# def register_user(username, password, role):
#     """Registers a new user in the database."""
#     try:
#         connection = create_connection()
#         if connection:
#             cursor = connection.cursor()
#             query = "INSERT INTO users (username, password, role) VALUES (%s, %s, %s)"
#             cursor.execute(query, (username, password, role))
#             connection.commit()
#             st.success("User registered successfully!")
#     except mysql.connector.Error as e:
#         st.error(f"Error registering user: {e}")
#     finally:
#         if connection and connection.is_connected():
#             cursor.close()
#             connection.close()
#
# def authenticate_user(username, password):
#     """Authenticates a user based on username and password."""
#     try:
#         connection = create_connection()
#         if connection:
#             cursor = connection.cursor(dictionary=True)
#             query = "SELECT * FROM users WHERE username = %s AND password = %s"
#             cursor.execute(query, (username, password))
#             user = cursor.fetchone()
#             return user
#     except mysql.connector.Error as e:
#         st.error(f"Error during authentication: {e}")
#         return None
#     finally:
#         if connection and connection.is_connected():
#             cursor.close()
#             connection.close()
