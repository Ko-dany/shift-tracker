import pandas as pd

def process_shift_data(file_path):
    print(f"Processing shift data from \"{file_path}\"")

    data = pd.read_excel(file_path)
    print(data.head())
    