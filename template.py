import os
from pathlib import Path
import logging


logging.basicConfig(level=logging.INFO,format ='[%(asctime)s]: %(message)s:')

project_name = 'Kidney-Disease-Classifier'

list_of_files = [
    ".github/workflows/.gitkeep", # if we keep empty git  not commit
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py"
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirments.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html"

]

#creating folders and files
for filepath in list_of_files:
    filepath= Path(filepath)
    filedir,filename = os.path.split(filepath)

    if filedir !="":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"creating Directory : {filedir} for the file : {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath,"w") as f:
            pass
            logging.info(f"creating empty file : {filepath}")
    
    else:
        logging.info(f"{filename} is already exists")