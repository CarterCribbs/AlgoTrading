


import os
import pandas_datareader.data as web
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

pd.set_option('display.width', 1000)

#c = p.Client(api_token= 'pk_e8c8520d3a3b4d15a481875b21b02419', version='stable')


start_date = '2014-01-01'
end_date = '2018-01-01'
goog_data = web.DataReader('GOOG', 'iex', start_date, end_date, api_key= 'sk_67c6cb84001f45aabe2e546b69a558cb')

#print(goog_data)



goog_data_signal = pd.DataFrame(index=goog_data.index)

goog_data_signal['price'] = goog_data['close']
goog_data_signal['daily_difference'] = goog_data_signal['price'].diff()


goog_data_signal['signal'] = 0.0
goog_data_signal['signal'] = np.where(goog_data_signal['daily_difference'][:]>0, 1.0, 0.0)


#LIMIT AMOUNT OF ORDERS:
#when the position column is +1.0 it means we should buy 1 share
#when the postiion column is -1.0 it means we should sell 1 share
#this is b/c the singla column when from 1.0 to 0 which means the stock is now declining
goog_data_signal['positions'] = goog_data_signal['signal'].diff()

#print(goog_data_signal.head(10))


#SIGNAL VISUALIZATION

#define a figure that will contain our chart
fig = plt.figure()
ax1 = fig.add_subplot(111, ylabel= 'Google price in $')
#plot price within range of days we choose
goog_data_signal['price'].plot(ax=ax1, color='r', lw=2)
#draw an up arrow when we buy one Google share and down arrow when selling
ax1.plot(goog_data_signal.loc[goog_data_signal.positions==1.0].index, goog_data_signal.price[goog_data_signal.positions==1.0], '^', markersize=5, color = 'm')
ax1.plot(goog_data_signal.loc[goog_data_signal.positions== -1.0].index, goog_data_signal.price[goog_data_signal.positions== -1.0], 'v', markersize=5, color='k')

#plt.show()


