import pandas as pd
import json
import requests
from .registry import DATASETS

def load_dataset(name):
    if name not in DATASETS:
        raise ValueError(f"Dataset '{name}' not found in registry.")
    
    metadata = DATASETS[name]
    if metadata["format"] == "csv":
        # Download and load CSV
        response = requests.get(metadata["file_url"])
        response.raise_for_status()
        return pd.read_csv(metadata["file_url"])
    elif metadata["format"] == "json":
        # Download and load JSON
        response = requests.get(metadata["file_url"])
        response.raise_for_status()
        # return pd.read_csv(metadata["url"])
        return json.load(metadata["file_url"])
    else:
        raise ValueError(f"Unsupported format: {metadata['format']}")
