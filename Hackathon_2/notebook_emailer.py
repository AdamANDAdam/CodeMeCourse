#Adam Surmiak, classroom management/emailer
import pandas as pd
import numpy as np

def text_import():

def data_import():

    df = pd.read_excel('class.xlsx')
    t = df.columns.ravel()
    k = df[t[0]].tolist()
    k = k[0:30]
    print(k)

def main():
    data_import()

if __name__ == '__main__':
    main()
