num_periods_fast = 10 # fast EMA time period
K_fast = 2 / (num_periods_fast + 1) # fast EMA smoothing factor
ema_fast = 0

num_periods_slow = 40 # slow EMA time period
K_slow = 2 / (num_periods_slow + 1) # slow EMA smoothing factor
ema_slow = 0

num_periods_macd = 20 # MACD EMA time period
K_macd = 2 / (num_periods_macd + 1) # MACD EMA smoothing factor
ema_macd = 0

ema_fast_values = [] # track fast EMA values for visualization purposes
ema_slow_values = [] # track slow EMA values for visualization purposes
macd_values = [] # track MACD values for visualization purposes
macd_signal_values = [] # MACD EMA values tracker

macd_histogram_values = [] # MACD - MACD-EMA

for close_price in close:
 if (ema_fast == 0): # first observation
   ema_fast = close_price
   ema_slow = close_price
 else:
   ema_fast = (close_price - ema_fast) * K_fast + ema_fast
   ema_slow = (close_price - ema_slow) * K_slow + ema_slow

 ema_fast_values.append(ema_fast)
 ema_slow_values.append(ema_slow)
 macd = ema_fast - ema_slow # MACD is fast_MA - slow_EMA

 if ema_macd == 0:
   ema_macd = macd
 else:
   ema_macd = (macd - ema_macd) * K_slow + ema_macd # signal is EMA of MACD values

 macd_values.append(macd)
 macd_signal_values.append(ema_macd)
 macd_histogram_values.append(macd - ema_macd)