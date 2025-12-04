import logging
import sys

def setDebugLogger(logger):
    logger.setLevel(logging.DEBUG)
    
    console_handler = logging.StreamHandler(stream=sys.stdout)
    console_handler.setLevel(logging.DEBUG)
    logger.addHandler(console_handler)
    
    return logger
