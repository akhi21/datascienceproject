import os 
import yaml
from src.datascience import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
from box.exceptions import BoxValueError

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """Reads a yaml file and returns a ConfigBox object.

    Args:
        path_to_yaml (Path): Path to the yaml file.

    Returns:
        ValueError: If the yaml file is empty.
        e: empty file
        ConfigBox: ConfigBox object containing the yaml data.
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
    

@ensure_annotations
def create_directories(path_to_directories: list, verbose: bool = True):
    """Creates a list of directories.

    Args:
        path_to_directories (list[Path]): List of paths to directories.

    Returns:
        None
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}")

@ensure_annotations
def save_json(path: Path, data: dict):
    """Saves a dictionary to a json file.

    Args:
        path (Path): Path to the json file.
        data (dict): Data to be saved.

    Returns:
        None
    """
    with open(path, "w") as f:
        json.dump(data, f, indent=4)

    logger.info(f"json file saved at: {path}")

@ensure_annotations
def load_json(path: Path) -> dict:
    """Loads a json file and returns a dictionary.

    Args:
        path (Path): Path to the json file.

    Returns:
        ConfigBox: data as class attributes instead of dictionary keys.
    """
    with open(path) as f:
        content = json.load(f)
    logger.info(f"json file loaded from: {path}")
    return ConfigBox(content)

@ensure_annotations
def save_bin(data: Any, path: Path):
    """Saves data in binary format using joblib.

    Args:
        data (Any): Data to be saved.
        path (Path): Path to the binary file.
    """
    joblib.dump(value=data, filename=path)
    logger.info(f"binary file saved at: {path}")
    
@ensure_annotations
def load_bin(path: Path) -> Any:
    """Loads data from a binary file using joblib.

    Args:
        path (Path): Path to the binary file. 

    Returns:
        Any: object stored in the file.   
    """
    data = joblib.load(path)
    logger.info(f"binary file loaded from: {path}")
    return data    