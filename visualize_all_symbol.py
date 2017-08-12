from datetime import date
import datetime
import pandas_datareader as pdr
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import talib
import os
import sys
sys.path.append('.')
import important_module


# main module
if __name__ == "__main__":

    s1 = date(2010,1,1)
    e1 = date(2017,8,1)

    dir = r'./csvData'
    f = open('symbol_list.csv', 'r')
    counter = 0

    # to read the symbol from symbol_list.csv file
    for line in f:
        symb = line.strip('\n')
        symb_file = os.path.join(dir, symb + '.csv')
        if not os.path.isfile(symb_file):
            print ("File "+symb_file + " is not present. Please download it first.")

        data_df = pd.read_csv(symb_file, sep=',', header=0, index_col=0, parse_dates=['Date'])
        data_df = important_module.adjustment_module(data_df)

        close = data_df['Close']
        c = np.array(close)
        output = talib.SMA(c, timeperiod=30)
        output2 = talib.SMA(c, timeperiod=100)

        real = talib.PPO(c, fastperiod=12, slowperiod=26, matype=0)
        buy_idx = pd.Series(real, index=close.index)
        sell_idx = buy_idx.copy(deep=True)

        buy_idx[buy_idx > 0] = 1
        buy_idx[buy_idx < 0] = 0
        buy_idx = buy_idx - buy_idx.shift()
        buy_idx[buy_idx < 0] = 0
        buy_idx[buy_idx == 0] = np.nan
        buy_idx = buy_idx.dropna()
        print('BUY ', buy_idx.index[-1])

        # sell_idx = pd.Series(real, index=close.index)
        sell_idx[sell_idx < 0] = -1
        sell_idx[sell_idx > 0] = 0
        sell_idx = abs(sell_idx)
        sell_idx = sell_idx - sell_idx.shift()
        sell_idx[sell_idx < 0] = 0
        sell_idx[sell_idx == 0] = np.nan
        sell_idx = sell_idx.dropna()
        print('SELL ', sell_idx.index[-1])
        # print len(index_series)

        plt.plot(data_df[['Close']])
        plt.plot(close.index, output)
        plt.plot(close.index, output2)
        plt.ylabel('price')
        plt.title(symb)
        plt.show()

        startDate = (datetime.datetime.today() - datetime.timedelta(365)).date()
        endDate = date.today()
        data_df['sma_1'] = pd.Series(output, index=close.index)
        data_df['sma_2'] = pd.Series(output2, index=close.index)
        data_df = data_df[startDate:endDate]
        buy_idx = buy_idx[startDate:endDate]
        sell_idx = sell_idx[startDate:endDate]

        plt.plot(data_df[['Close']])
        plt.plot(data_df[['sma_1']])
        plt.plot(data_df[['sma_2']])
        [plt.axvline(_x, color='g') for _x in np.array(buy_idx.index)]
        [plt.axvline(_x, color='r') for _x in np.array(sell_idx.index)]
        plt.ylabel('price')
        plt.title(symb)
        plt.show()


