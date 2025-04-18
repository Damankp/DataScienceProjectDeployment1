import os
import yaml
from src.datascience.logger import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
from box.exceptions import BoxValueError

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    Reads a YAML file and returns its content as a ConfigBox object.
    
    Args:
        path_to_yaml (str): Path to the YAML file.

    Raises:
        ValueError: If the yaml file is empty
        e: empty file
        
    Returns:
        ConfigBox: Content of the YAML file as a ConfigBox object.
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"YAML file loaded successfully from {path_to_yaml}")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")    
    except Exception as e:
        raise e
    

@ensure_annotations
def create_directories(path_to_dirs: list, verbose=True):
    """
    Create directories if they do not exist.

    Args:
        path_to_dirs (list): List of directory paths to create.
        verbose (bool): If True, print the created directories.
    """
    for dir_path in path_to_dirs:
        os.makedirs(dir_path, exist_ok=True)
        if verbose:
            logger.info(f"Created directory: {dir_path}")

@ensure_annotations
def save_json(path: Path, data: dict):
    """
    Save a dictionary as a JSON file.

    Args:
        path (Path): Path to save the JSON file.
        data (dict): Dictionary to save.
    """
    with open(path, "w") as json_file:
        json.dump(data, json_file, indent=4)

    logger.info(f"JSON file saved at {path}")


@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """
    Load a JSON file and return its content as a dictionary.

    Args:
        path (Path): Path to the JSON file.

    Returns:
        ConfigBox: Data as class attributes instead of dict.
    """
    with open(path, "r") as json_file:
        data = json.load(json_file)
        
    logger.info(f"JSON file loaded from {path}")
    return data

@ensure_annotations
def save_bin(data: Any, path: Path):
    """
    Save binary file.

    Args:
        data (Any): Data to be saved as binary.
        path (Path): Path to binary file.
    """
    joblib.dump(value=data, filename=path)
    logger.info(f"binary file saved at {path}")

@ensure_annotations
def load_bin(path: Path) -> Any:
    """
    Load binary file.

    Args:
        path (Path): Path to binary file.

    Returns:
        Any: Loaded data.
    """
    data = joblib.load(path)
    logger.info(f"binary file loaded from {path}")
    return data