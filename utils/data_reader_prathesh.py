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
    elif format.lower() in ['excel', 'xlsx']: return read_excel_data(file_path, sheet_name)
    else: raise ValueError(f"Unsupported format: {format}")

#
# from openpyxl import load_workbook
#
#
# def read_excel_data(file_path: str) -> List[tuple]:
#     data = []
#
#     if not os.path.exists(file_path):
#         return data
#
#     workbook = load_workbook(file_path)
#     sheet = workbook.active  # reads first sheet
#
#     # Get headers from first row
#     headers = [cell.value for cell in sheet[1]]
#
#     # Read remaining rows
#     for row in sheet.iter_rows(min_row=2, values_only=True):
#         data.append(tuple(row))
#
#     return datax

import pandas as pd

def read_excel_data(file_path, sheet_name):
    df = pd.read_excel(file_path, sheet_name=sheet_name)

    data = [tuple(row) for row in df.values]

    return data
