import statistics as stats
import math as math
import pandas as pd

SRC_File = "tsla_data.pkl"

tsla_data = pd.read_pickle(SRC_File)

close = tsla_data["close"]

time_length = 20
historical_values = []
sma_values = []
std_dev_values = []

for closing_price in close:
    historical_values.append(closing_price)
    if len(historical_values)>time_length:
        del historical_values[0]
    sma = stats.mean(historical_values)
    sma_values.append(sma)

    variance = 0
    for value in historical_values:
        variance += (value-sma)**2
    std_dev = math.sqrt(variance)
    std_dev_values.append(std_dev)

tsla_data = tsla_data.assign(ClosePrice=pd.Series(close, index=tsla_data.index))
tsla_data = tsla_data.assign(StandardDeviationOver20Days=pd.Series(std_dev_values, index=tsla_data.index))
close_price = tsla_data['ClosePrice']
stddev = tsla_data['StandardDeviationOver20Days']

import matplotlib.pyplot as plt

fig = plt.figure()
ax1 = fig.add_subplot(211, ylabel='Tesla price in $')
close_price.plot(ax=ax1, color='g', lw=2., legend=True)
ax2 = fig.add_subplot(212, ylabel='Stddev in $')
stddev.plot(ax=ax2, color='b', lw=2., legend=True)
plt.show()