import csv
import json
import os
from typing import List, Dict, Any

# Optional pandas import for Excel support
try:
    import pandas as pd
except ImportError:
    pd = None  # pandas is optional; will raise informative error if used without installation
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
    if not os.path.exists(file_path):
        return []
    with open(file_path, 'r') as jsonfile:
        data = json.load(jsonfile)
    return data if isinstance(data, list) else [data]

def read_excel_data(file_path: str) -> List[Dict[str, Any]]:
    """Read Excel file and return list of row dictionaries.

    Requires pandas. If pandas is not installed, raises ImportError with guidance.
    """
    if pd is None:
        raise ImportError("pandas is required for Excel support. Install it via 'pip install pandas'.")
    if not os.path.exists(file_path):
        return []
    df = pd.read_excel(file_path)
    # Convert DataFrame to list of dicts (records)
    return df.to_dict(orient='records')
    if not os.path.exists(file_path): return []
    with open(file_path, 'r') as jsonfile:
        data = json.load(jsonfile)
    return data if isinstance(data, list) else [data]

def read_test_data(file_path: str, format: str = 'csv') -> List:
    fmt = format.lower()
    if fmt == 'csv':
        return read_csv_data(file_path)
    elif fmt == 'json':
        return read_json_data(file_path)
    elif fmt == 'excel':
        return read_excel_data(file_path)
    else:
        raise ValueError(f"Unsupported format: {format}")
    if format.lower() == 'csv': return read_csv_data(file_path)
    elif format.lower() == 'json': return read_json_data(file_path)
    else: raise ValueError(f"Unsupported format: {format}")
