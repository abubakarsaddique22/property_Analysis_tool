import os 
import logging
from pathlib import Path

# Set up logging
logging.basicConfig(level=logging.INFO)


project_name='mlproject'

# create list of requirment files
list_of_files=[
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/components/data_ingestion.py",
    f"src/{project_name}/components/data_transformation.py",
    f"src/{project_name}/components/model_tranier.py",
    f"src/{project_name}/components/model_monitering.py",
    f"src/{project_name}/pipelines/__init__.py",
    f"src/{project_name}/pipelines/training_pipeline.py",
    f"src/{project_name}/pipelines/prediction_pipeline.py",
    f"src/{project_name}/exception.py",
    f"src/{project_name}/logger.py",
    f"src/{project_name}/utils.py",
    "main.py",
    "app.py",
    "requirements.txt",
    "setup.py"
]

# Iterating Through the List to Create Directories & Files

for filepath in list_of_files:
    filepath = Path(filepath)  # Convert string to Path object
    filedir, filename = os.path.split(filepath)  # Extract directory and filename

    # Creating Necessary Directories

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory:{filedir} for the file {filename}")

    #  Creating Empty Files If They Don’t Exist
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as f:
            pass  # Creates an empty file
        logging.info(f"Creating empty file: {filepath}")
    else: # Handling Already Existing Files
        logging.info(f"{filename} already exists")


