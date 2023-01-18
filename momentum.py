import pandas as pd

SRC_File = "tsla_data.pkl"

tsla_data = pd.read_pickle(SRC_File)

close = tsla_data["close"]
time_period = 20
history=[]
momentum_values = []

for close_price in close:
    history.append(close_price)
    if len(history) > time_period:
        del history[0]

    momentum = close_price - history[0] # difference in close price and specified days ago price (time_period days ago)
    momentum_values.append(momentum)


tsla_data = tsla_data.assign(ClosePrice=pd.Series(close, index=tsla_data.index))
tsla_data = tsla_data.assign(MomentumFromPrice20DaysAgo=pd.Series(momentum_values, index=tsla_data.index))
close_price = tsla_data['ClosePrice']
mom = tsla_data['MomentumFromPrice20DaysAgo']

import matplotlib.pyplot as plt

fig = plt.figure()
ax1 = fig.add_subplot(211, ylabel='Tesla price in $')
close_price.plot(ax=ax1, color='g', lw=2., legend=True)
ax2 = fig.add_subplot(212, ylabel='Momentum in $')
mom.plot(ax=ax2, color='b', lw=2., legend=True)
plt.show()