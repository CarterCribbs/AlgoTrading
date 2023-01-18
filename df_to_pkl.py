import pandas_datareader.data as web
import pandas as pd

pd.set_option('display.width', 1000)

start_date = '2022-01-13'
end_date = '2023-01-13'
goog_data = web.DataReader('GOOG', 'iex', start_date, end_date, api_key= 'sk_67c6cb84001f45aabe2e546b69a558cb')

goog_data.to_pickle('tsla_data.pkl')

df = pd.read_pickle('tsla_data.pkl')
print(df)