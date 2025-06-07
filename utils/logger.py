import logging
import os

def get_logger(name: str):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    os.makedirs("logs", exist_ok=True)
    file_handler = logging.FileHandler("logs/pipeline.log")
    formatter = logging.Formatter('%(asctime)s | %(name)s | %(levelname)s: %(message)s')

    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger
