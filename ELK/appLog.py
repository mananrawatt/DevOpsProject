# import logging
#
# # Configure logging
# def setup_logging():
#     # Create a custom logger
#     logger = logging.getLogger(__name__)
#     logger.setLevel(logging.INFO)
#
#     # Create a file handler
#     handler = logging.FileHandler('app.log')
#     handler.setLevel(logging.INFO)
#
#     # Create a formatter and set it for the handler
#     formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
#     handler.setFormatter(formatter)
#
#     # Add the file handler to the logger
#     logger.addHandler(handler)
#
#     return logger
#
# # Initialize logging
# logger = setup_logging()
import logging
from logConfig import setup_logging

# Initialize logging
logger = setup_logging()

# Example usage of the logger
logger.info("Streamlit app configuration set.")
logger.info("Local CSS file style.css loaded.")
logger.info("User selected menu option: Jenkins.")
logger.info("Displaying Jenkins section.")
