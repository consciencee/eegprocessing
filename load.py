import csv
import pandas as pd

def load_ecg_as_list(filename):
    input_file = open(filename, 'rb')
    csv_input = csv.DictReader(input_file, fieldnames=['Time', 'ECG'])
    row_cnt = 0
    ecg_data = []
    for row in csv_input:
        if(row_cnt > 0):
            ecg_data.append(row['ECG'])
        row_cnt += 1

    return ecg_data

def load_ecg_as_df(filename):
    df = pd.read_csv(filename)
    return df