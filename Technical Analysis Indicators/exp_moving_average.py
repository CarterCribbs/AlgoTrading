import pandas as pd 
import matplotlib.pyplot as plt
import statistics as stats

SRC_DATA_FILENAME = "goog_test_data.pkl"

goog_ema = pd.read_pickle(SRC_DATA_FILENAME)

num_periods = 20
K = 1 / (num_periods+1)
ema_p = 0 
ema_values = []

close = goog_ema["close"]

for closing_price in close:
    if ema_p==0 :
        ema_p = closing_price
    else:
        ema_p = (closing_price - ema_p) * K + ema_p

    ema_values.append(ema_p)

goog_ema = goog_ema.assign(ClosePrice = pd.Series(close, index=goog_ema.index))
goog_ema = goog_ema.assign(Exp120DayMovingAverage = pd.Series(ema_values, index=goog_ema.index))


close_price = goog_ema['ClosePrice']
ema = goog_ema['Exp120DayMovingAverage']

fig = plt.figure()
ax1 = fig.add_subplot(111, ylabel='Google price in $')
close_price.plot(ax=ax1, color='g', lw=2., legend=True)
ema.plot(ax=ax1, color='r', lw=2., legend=True)
plt.show()


