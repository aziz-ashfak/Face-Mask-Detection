import logging
from datetime import datetime
import os 
import sys


logs_file = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path = os.path.join(os.getcwd(),'logs')

os.makedirs(logs_path,exist_ok=True)

logs_file_path = os.path.join(logs_path,logs_file)

logging.basicConfig(
    format="[%(asctime)s - %(lineno)d %(message)s]",
    level=logging.INFO,
    handlers= [
        logging.FileHandler(logs_file_path),
        logging.StreamHandler(sys.stdout)
    ]
    
)