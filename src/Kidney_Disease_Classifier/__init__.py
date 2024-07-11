#logger file

import os 
import sys
import logging

# Create a logger
logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

log_dir = "logs"
log_filepath = os.path.join(log_dir,"my_logs.log")
os.makedirs(log_dir,exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format=logging_str,
    handlers=[
        logging.FileHandler(log_filepath),  #to write  log messages to a specified file 
        logging.StreamHandler(sys.stdout) #responsible for directing log messages to an output stream (the console) (stdout or stderr)
    ]            
)

logger = logging.getLogger("kidneyClassifierLogger") #retrieve a logger instance with the specified name

