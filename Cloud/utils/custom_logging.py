import logging
import os
from datetime import datetime
from typing import Optional
from logging.handlers import RotatingFileHandler

def setup_logging(
    script_name: str,
    log_dir: str = 'logs',
    log_level: int = logging.INFO,
    max_bytes: int = 10485760,  # 10MB
    backup_count: int = 5
) -> logging.Logger:
    """
    Sets up logging to both the console and a log file with rotation.

    Args:
        script_name (str): Name of the script being run, used in log filename.
        log_dir (str): The directory where log files should be stored. Defaults to 'Cloud/Logs'.
        log_level (int): The logging level to use. Defaults to logging.INFO.
        max_bytes (int): Maximum size of each log file in bytes. Defaults to 10MB.
        backup_count (int): Number of backup files to keep. Defaults to 5.

    Returns:
        logging.Logger: Configured logger instance
    """
    # Ensure the directory exists
    os.makedirs(log_dir, exist_ok=True)
    
    # Generate a logfile name with a timestamp and script name
    current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    log_filename = os.path.join(log_dir, f"{script_name}_{current_time}.log")

    # Create a custom logger
    logger = logging.getLogger('reddit_pipeline')
    logger.setLevel(log_level)

    # Remove any existing handlers
    logger.handlers = []

    # Create handlers
    # Rotating file handler
    file_handler = RotatingFileHandler(
        log_filename,
        maxBytes=max_bytes,
        backupCount=backup_count,
        encoding='utf-8'
    )
    file_handler.setLevel(log_level)

    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(log_level)

    # Create formatters and add it to handlers
    log_format = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - [%(filename)s:%(lineno)d] - %(message)s'
    )
    file_handler.setFormatter(log_format)
    console_handler.setFormatter(log_format)

    # Add handlers to the logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    # Prevent the log messages from being propagated to the root logger
    logger.propagate = False

    logger.info(f"Logging setup successfully. Logs will be outputted to {log_filename}")
    
    return logger

def get_logger(name: Optional[str] = None) -> logging.Logger:
    """
    Gets a logger instance with the specified name.

    Args:
        name (Optional[str]): The name of the logger. 
            If None, returns the reddit_pipeline logger.

    Returns:
        logging.Logger: The logger instance.
    """
    if name is None:
        return logging.getLogger('reddit_pipeline')
    return logging.getLogger(f'reddit_pipeline.{name}')

if __name__ == '__main__':
    # Test the logging setup
    logger = setup_logging()
    logger.debug("This is a debug message")
    logger.info("This is an info message")
    logger.warning("This is a warning message")
    logger.error("This is an error message")
    logger.critical("This is a critical message")