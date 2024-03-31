import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s')

project_name= "CIFAR10_Classification"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/components/data_ingestion.py",
    f"src/{project_name}/components/model_evaluator.py",
    f"src/{project_name}/components/model_trainer.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/constants/__init__.py",
    f"src/{project_name}/models/__init__.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/pipeline/stage_01_data_ingestion.py",
    f"src/{project_name}/pipeline/stage_02_model_trainer.py",
    f"src/{project_name}/pipeline/stage_03_model_evaluator.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    "artifacts/raw",
    "artifacts/processed",
    "logs",
    "notebooks/research.ipynb",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "templates",
    "static",
    "scores.json",
    "main.py",

    ]

for filepath in list_of_files:
    filepath = Path(filepath)
    if not filepath.parent.exists():
        logging.info(f"Creating directory: {filepath.parent}")
        os.makedirs(filepath.parent)
    else:
        logging.info(f"Directory already exists: {filepath.parent}")
    if not filepath.exists():
        logging.info(f"Creating file: {filepath}")
        filepath.touch()
    else:
        logging.info(f"File already exists: {filepath}")


