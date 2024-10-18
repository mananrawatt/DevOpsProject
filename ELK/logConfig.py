import logging
import os

def setup_logging():
    # Define the log directory and create it if it doesn't exist
    log_directory = 'logs'
    if not os.path.exists(log_directory):
        os.makedirs(log_directory)

    # Define the log file path
    log_file_path = os.path.join(log_directory, 'app.log')

    # Create a logger
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)  # Set the lowest level of logging to DEBUG

    # Create handlers
    # Use 'a' mode to append to the same log file
    file_handler = logging.FileHandler(log_file_path, mode='a')  # Append mode
    console_handler = logging.StreamHandler()

    # Set the log level for handlers
    file_handler.setLevel(logging.DEBUG)
    console_handler.setLevel(logging.DEBUG)

    # Create formatters and add them to handlers
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    # Add handlers to the logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
