import pandas as pd
import pandas_datareader.data as web
import statistics as stats
import matplotlib.pyplot as plt

SRC_DATA_FILENAME = 'goog_test_data.pkl'

goog_data2 = pd.read_pickle(SRC_DATA_FILENAME)

goog_data_2_tail = goog_data2.tail(620)

close = goog_data_2_tail['close']


sma_time_period = 20
history = [] # historical prices
sma_list = [] # simple moving average list 

for closing_price in close:
    history.append(closing_price)
    if len(history) > sma_time_period:
        del (history[0])
    sma_list.append(stats.mean(history))

goog_data_2_tail = goog_data_2_tail.assign(ClosePrice=pd.Series(close, index=goog_data_2_tail.index))
goog_data_2_tail = goog_data_2_tail.assign(Simple20DayMovingAverage=pd.Series(sma_list, index=goog_data_2_tail.index))

close_price=goog_data_2_tail['ClosePrice']
sma_list=goog_data_2_tail['Simple20DayMovingAverage']


fig = plt.figure()
ax1 = fig.add_subplot(111, ylabel='Google price in $')
close_price.plot(ax=ax1, color='g', lw=2., legend=True)
sma_list.plot(ax=ax1, color='r', lw=2., legend=True)
plt.show()

    

