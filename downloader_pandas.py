from datetime import date
import pandas_datareader as pdr
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import talib
import sys
sys.path.append('.')
import important_module


s1 = date(2010,1,1)
e1 = date(2017,8,1)
symb = 'SBIN.NS'

# data_df = pdr.get_data_yahoo(symbols=symb, start=s1, end=e1)
# data_df.to_csv(symb+'.csv')
data_df = pd.read_csv(symb+'.csv', sep=',', header=0, index_col=0, parse_dates=['Date'])
data_df = important_module.adjustment_module(data_df)

input_arrays = important_module.df_to_dic_array(data_df)
print(input_arrays)
from talib.abstract import *
output = SMA(input_arrays, timeperiod=25) # calculate on close prices by default
output = SMA(input_arrays, timeperiod=25, price='open') # calculate on opens
upper, middle, lower = BBANDS(input_arrays, 20, 2, 2)
slowk, slowd = STOCH(input_arrays, 5, 3, 0, 3, 0) # uses high, low, close by default
# slowk, slowd = STOCH(input_arrays, 5, 3, 0, 3, 0, prices=['high', 'low', 'open'])
real = PPO(input_arrays, fastperiod=12, slowperiod=26, matype=0)

plt.figure()
plt.plot(data_df.index, upper)
plt.plot(data_df.index, middle)
plt.plot(data_df.index, lower)
plt.ylabel('price')
plt.show()

plt.figure()
plt.plot(data_df.index, slowk)
plt.plot(data_df.index, slowd)
plt.ylabel('price')
plt.show()

plt.figure()
plt.plot(data_df[['Close']])
plt.plot(data_df.index, output)
plt.ylabel('price')
plt.show()

plt.figure()
plt.plot(data_df[['Close']])
plt.ylabel('price')
plt.show()
#
# close = data['Close']
# c = np.array(close)
# output = talib.SMA(c)
#
# plt.plot(data[['Close']])
# plt.plot(close.index, output)
# plt.ylabel('price')
# plt.show()
#
# stk_sma = pd.DataFrame(output, columns=['Close'],index=close.index)
#
# sma = data[['Close']] - stk_sma


#for index, row in sma.iterrows():