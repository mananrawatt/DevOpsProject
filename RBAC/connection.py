import mysql.connector
from mysql.connector import Error
import streamlit as st

def create_connection():
    try:
        connection = mysql.connector.connect(
            host="localhost",          # Change to your MySQL host if needed
            user="root",      # Your MySQL username
            password="root12@M",  # Your MySQL password
            database="rbac_user" # Database you created
        )
        if connection.is_connected():
            st.write("Connected to MySQL database!")
        return connection
    except Error as e:
        st.error(f"Error connecting to MySQL: {e}")
        return None
