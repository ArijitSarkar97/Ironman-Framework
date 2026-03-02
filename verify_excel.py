import os
from utils.data_reader import read_excel_data, read_test_data

def main():
    # Path to sample Excel file
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), 'test-data'))
    excel_path = os.path.join(base_dir, 'checkout_test_data.xlsx')
    if not os.path.exists(excel_path):
        raise FileNotFoundError(f"Excel file not found at {excel_path}")
    print('Reading via read_excel_data...')
    data1 = read_excel_data(excel_path)
    print(f"Rows read: {len(data1)}")
    print('Reading via read_test_data (format=excel)...')
    data2 = read_test_data(excel_path, format='excel')
    print(f"Rows read: {len(data2)}")
    assert data1 == data2, "Data mismatch between functions"
    print('Success: Both methods return identical data.')

if __name__ == '__main__':
    main()
