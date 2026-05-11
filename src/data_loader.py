import pandas as pd

def data_loading(file1,file2):
    data1 = pd.read_csv(file1)
    data2 = pd.read_csv(file2)
    return data1, data2