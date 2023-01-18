#here we will be handling time series data
import datetime as dt
import pandas as pd
import random

# this is example time-series data as a list of dictionary objects
time_series_data = \
[{'date': dt.datetime(2019, 11, 13, 9, 0),   
  'open': 71.8075, 'high': 71.845,  'low': 71.7775, 
  'close': 71.7925, 'volume': 219512},
{'date': dt.datetime(2019, 11, 13, 9, 15),  
 'open': 71.7925, 'high': 71.8,    'low': 71.78,   
 'close': 71.7925, 'volume': 59252},
{'date': dt.datetime(2019, 11, 13, 9, 30),  
 'open': 71.7925, 'high': 71.8125, 'low': 71.76,
 'close': 71.7625, 'volume': 57187},
{'date': dt.datetime(2019, 11, 13, 9, 45),  
 'open': 71.76,   'high': 71.765,  'low': 71.735,  
 'close': 71.7425, 'volume': 43048}, 
{'date': dt.datetime(2019, 11, 13, 10, 0),  
 'open': 71.7425, 'high': 71.78,   'low': 71.7425, 
 'close': 71.7775, 'volume': 45863},
{'date': dt.datetime(2019, 11, 13, 10, 15), 
 'open': 71.775,  'high': 71.8225, 'low': 71.77,   
 'close': 71.815,  'volume': 42460},
{'date': dt.datetime(2019, 11, 13, 10, 30), 
 'open': 71.815,  'high': 71.83,   'low': 71.7775, 
 'close': 71.78,   'volume': 62403},
{'date': dt.datetime(2019, 11, 13, 10, 45), 
 'open': 71.775,  'high': 71.7875, 'low': 71.7475,
 'close': 71.7525, 'volume': 34090},
{'date': dt.datetime(2019, 11, 13, 11, 0),  
 'open': 71.7525, 'high': 71.7825, 'low': 71.7475,
 'close': 71.7625, 'volume': 39320},
{'date': dt.datetime(2019, 11, 13, 11, 15), 
 'open': 71.7625, 'high': 71.7925, 'low': 71.76,
 'close': 71.7875, 'volume': 20190}]

 #Create new DF from time_series_data 
df = pd.DataFrame(time_series_data)
#print(df)

#print(df.columns.tolist())

rearranged =pd.DataFrame(time_series_data, columns=['close', 'date', 'open', 'high', 'low', 'volume'])

#print(rearranged)

#renaming date column 
df.rename(columns={'date':'timestamp'}, inplace=True)
#print(df)

#reversingi rows 
df[::-1]

#print(df.iloc[:,4])

#Modify values in timestamp column 
df['timestamp'] = df['timestamp'].apply(lambda x: x.strftime("%d-%m%Y %H:%M:%S"))
print(df)

#create new df by a desired column in ascending or decending order
df.sort_values(by='close', ascending=True)

#finding the average 
for _, row in df.iterrows():
    avg= (row['open']+row['close']+row['high']+row['low'])/4
    #print(f"Index:{_} | Average: {avg}")

#iterating column-wise over all the values of the first row of df
for value in df.iloc[0]:
    print(value)

#to create new Dataframe by concatenation
# pandas.concat([df, df_new]).reset_index(drop=True)


