import pandas as pd 
from pandas_datareader import data
import numpy as np
from sklearn.model_selection import train_test_split


def load_financial_data(start_date, end_date, output_file):
    try:
        df = pd.read_pickle(output_file)
        print('File data found...reading GOOG data')
    except FileNotFoundError:
        print('File not found...downloading the GOOG data')
        df = data.DataReader('GOOG', 'iex', start_date, end_date, api_key='sk_67c6cb84001f45aabe2e546b69a558cb')
        df.to_pickle(output_file)
    
    return df

#goog_data = load_financial_data(start_date='2008-01-01', end_date='2018-01-01', output_file='goog_data_large.pkl')


def create_classification_trading_condition(df):
    print(df)
    df['Open-Close'] = df.Open - df.Close
    df['High-Low'] = df.High - df.Low
    df = df.dropna()
    X = df [['Open-Close', 'High-Low']]
    Y = np.where(df['Close'].shift(-1)>df['Close'], 1, -1)
    
    return (X, Y)

def create_regression_trading_condition(df):
    df['Open-Close'] = df.Open - df.Close
    df['High-Low'] = df.High - df.Low
    df = df.dropna()
    X = df [['Open-Close', 'High-Low']]
    Y = df['Close'].shift(-1) - df['Close']
    
    return (X, Y)

mara_df = load_financial_data(start_date='2008-01-01', end_date='2018-01-01', output_file='mara_data.pkl')
test = create_classification_trading_condition(df = mara_df)


#Partitioning the data set 
def create_train_split_group(X, Y, split_ratio = 0.8):
    return train_test_split(X, Y, shuffle=False, train_size=split_ratio)