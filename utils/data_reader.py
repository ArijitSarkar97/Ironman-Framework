import csv
import json
import os
import openpyxl
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

def read_excel_data(file_path: str, sheet_name: str = None) -> List[tuple]:
    data = []
    if not os.path.exists(file_path): return data
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook[sheet_name] if sheet_name else workbook.active
    
    # Assuming first row is header, returning rows as tuples
    for row in sheet.iter_rows(min_row=2, values_only=True):
        data.append(tuple(row))
    print(data)
    return data

def read_test_data(file_path: str, format: str = 'csv', sheet_name: str = None) -> List:
    if format.lower() == 'csv': return read_csv_data(file_path)
    elif format.lower() == 'json': return read_json_data(file_path)
    elif format.lower() in ['excel', 'xlsx']: return read_excel_data(file_path, sheet_name)
    else: raise ValueError(f"Unsupported format: {format}")
