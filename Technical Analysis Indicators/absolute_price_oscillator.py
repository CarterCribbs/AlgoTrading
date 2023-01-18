import pandas as pd 
import matplotlib.pyplot as plt
import statistics as stats

SRC_DATA_FILENAME = "goog_test_data.pkl"

goog_apo = pd.read_pickle(SRC_DATA_FILENAME)

print(goog_apo)
num_periods_fast = 10
K_fast = 1 / (num_periods_fast+1)
ema_fast = 0 
ema_values_fast = []

num_periods_slow = 40
K_slow = 1 / (num_periods_slow+1)
ema_slow = 0
ema_values_slow = []

apo_values=[]

close = goog_apo["close"]

for closing_price in close:
    if ema_fast==0 :
        ema_fast = closing_price
        ema_slow = closing_price
    else:
        ema_fast = (closing_price - ema_fast) * K_fast + ema_fast
        ema_slow = (closing_price - ema_slow) * K_slow + ema_slow

    ema_values_fast.append(ema_fast)
    ema_values_slow.append(ema_slow)
    
    apo_values.append(ema_fast - ema_slow)

goog_apo = goog_apo.assign(ClosePrice = pd.Series(close, index=goog_apo.index))
goog_apo = goog_apo.assign(FastExp10DayMovingAverage = pd.Series(ema_values_fast, index=goog_apo.index))
goog_apo = goog_apo.assign(SlowExp40DayMovingAverage = pd.Series(ema_values_slow, index=goog_apo.index))
goog_apo = goog_apo.assign(AbsolutePriceOscillator = pd.Series(apo_values, index=goog_apo.index))



close_price = goog_apo['ClosePrice']
ema_fast_column = goog_apo['FastExp10DayMovingAverage']
ema_slow_column = goog_apo['SlowExp40DayMovingAverage']
apo_column = goog_apo['AbsolutePriceOscillator']

fig = plt.figure()
ax1 = fig.add_subplot(211, ylabel='Google price in $')
close_price.plot(ax=ax1, color='g', lw=2., legend=True)
ema_fast_column.plot(ax=ax1, color='b', lw=2., legend=True)
ema_slow_column.plot(ax=ax1, color='r', lw=2., legend=True)
ax2 = fig.add_subplot(212, ylabel='APO')
apo_column.plot(ax=ax2, color='r', lw=2., legend=True)

plt.show()
