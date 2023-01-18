import statistics as stats
import math as math
import pandas as pd 

SRC_File = "tsla_data.pkl"

goog_data = pd.read_pickle(SRC_File)

close = goog_data["close"]

time_period = 5
standard_dev_factor = 2
sma_history_tracker = []
upper_band_values = []
lower_band_values = []
sma_values = []

for closing_price in close:
    sma_history_tracker.append(closing_price)
    if len(sma_history_tracker) > time_period:
        del sma_history_tracker[0]
    sma_current = stats.mean(sma_history_tracker)
    sma_values.append(sma_current)

    variance = 0 

    for history_price in sma_history_tracker: 
        variance = variance + ((history_price - sma_current) **2)
    
    standard_deviation = math.sqrt(variance / time_period)
    upper_band_values.append(sma_current + (standard_deviation*standard_dev_factor))
    lower_band_values.append(sma_current - (standard_deviation*standard_dev_factor))


goog_data = goog_data.assign(ClosePrice=pd.Series(close, index=goog_data.index))
goog_data = goog_data.assign(MiddleBollingerBand20DaySMA=pd.Series(sma_values, index=goog_data.index))
goog_data = goog_data.assign(UpperBollingerBand20DaySMA2StdevFactor=pd.Series(upper_band_values, index=goog_data.index))
goog_data = goog_data.assign(LowerBollingerBand20DaySMA2StdevFactor=pd.Series(lower_band_values, index=goog_data.index))
close_price = goog_data['ClosePrice']
mband = goog_data['MiddleBollingerBand20DaySMA']
uband = goog_data['UpperBollingerBand20DaySMA2StdevFactor']
lband = goog_data['LowerBollingerBand20DaySMA2StdevFactor']

import matplotlib.pyplot as plt

fig = plt.figure()
ax1 = fig.add_subplot(111, ylabel='Google price in $')
close_price.plot(ax=ax1, color='g', lw=2., legend=True)
mband.plot(ax=ax1, color='b', lw=2., legend=True)
uband.plot(ax=ax1, color='y', lw=2., legend=True)
lband.plot(ax=ax1, color='r', lw=2., legend=True)
plt.show()