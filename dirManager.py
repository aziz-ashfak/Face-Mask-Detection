from pathlib import Path
import os
import sys 

dir_manager = [
    "src/__init__.py",
    "src/components/__init__.py",
    "src/pipeline/__init__.py",
    "src/utils/__init__.py",
    "src/constant/__init__.py",
    "src/logger.py",
    "src/exception.py",
    "config/config.yaml",
    "params/params.yaml",
    "Research/__init__.py",
    "main.py",
    "app.py"
]

for filepath in dir_manager:
    
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    
    if filedir != "":
       os.makedirs(filedir, exist_ok=True)
    
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        
        with open(filepath, "w") as file:
            pass