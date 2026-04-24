import os
import pytest
from utils.data_reader import read_excel_data, read_test_data


def test_read_excel_data():
    # Path to the sample Excel file in test-data directory
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    excel_path = os.path.join(base_dir, 'test-data', 'checkout_test_data.xlsx')
    # Ensure the file exists
    assert os.path.exists(excel_path), f"Excel file not found at {excel_path}"

    # Read using the dedicated function
    excel_data = read_excel_data(excel_path)
    # Read using the generic function with format='excel'
    generic_data = read_test_data(excel_path, format='excel')

    # Both methods should return the same data
    assert excel_data == generic_data
    # Basic sanity: should be a list of dicts and not empty
    assert isinstance(excel_data, list)
    assert len(excel_data) > 0
    assert isinstance(excel_data[0], dict)
