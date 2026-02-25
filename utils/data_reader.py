import csv
import json
import os
from typing import List, Dict, Any

def read_csv_data(file_path: str) -> List[tuple]:
    data = []
    if not os.path.exists(file_path): return data
    with open(file_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(tuple(row.values()))
    return data

def read_json_data(file_path: str) -> List[Dict[str, Any]]:
    if not os.path.exists(file_path): return []
    with open(file_path, 'r') as jsonfile:
        data = json.load(jsonfile)
    return data if isinstance(data, list) else [data]

def read_test_data(file_path: str, format: str = 'csv') -> List:
    if format.lower() == 'csv': return read_csv_data(file_path)
    elif format.lower() == 'json': return read_json_data(file_path)
    else: raise ValueError(f"Unsupported format: {format}")
