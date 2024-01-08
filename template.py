import os
import logging
from pathlib import Path

logging.basicConfig(
    filename="temp.log",  # Upon initiating the project, remove the temporary log file.
    level=logging.INFO,
    format="[%(asctime)s | %(levelname)s | %(message)s]",
)


while True:
    project_name = input("Enter your project name: ")
    if project_name != "":
        break

list_of_files = [
    ".github/workflows/.gitkeep",
    "research/notebook.ipynb",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/exception.py",
    f"src/{project_name}/logger.py",
    f"src/{project_name}/utils.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/components/data_ingestion.py",
    f"src/{project_name}/components/data_transformation.py",
    f"src/{project_name}/components/model_trainer.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/pipeline/predict_pipeline.py",
    f"src/{project_name}/pipeline/train_pipeline.py",
    "tests/__init__.py",
    "tests/integration/__init__.py",
    "tests/integration/test_integration.py",
    "tests/unit/__init__.py",
    "tests/unit/test_unit.py",
    "requirements.txt",
    "setup.py",
    "init_setup.sh",
    # Additional Config Files:
    "setup.cfg",
    "pyproject.toml",
    "tox.ini",
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating a directory at: {filedir} for file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as file:
            logging.info(f"Creating a new file: {filename} at path: {filepath}")

    else:
        logging.info(f"File already exists at: {filepath}")
