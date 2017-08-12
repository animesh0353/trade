from datetime import date
import pandas_datareader as pdr
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import talib
import os


def adjustment_module(data_df_copy):
    '''
    module to adjust the OHLCV based on Adjusted Close
    :param data_df_copy:
    :return data_df_copy:
    '''

    multiplier = data_df_copy['Adj Close'].divide(data_df_copy['Close'])
    data_df_copy = data_df_copy.drop('Adj Close', axis=1)
    vol = data_df_copy['Volume']
    data_df_copy = data_df_copy.drop('Volume', axis=1)
    data_df_copy = data_df_copy.multiply(multiplier, axis=0)

    vol = vol / multiplier
    data_df_copy['Volume'] = vol
    data_df_copy[data_df_copy == 0] = np.nan
    data_df_copy = data_df_copy.fillna(method='ffill')
    return data_df_copy


def df_to_dic_array(data_df):

    inputs = {
    'open': np.array(data_df['Open']),
    'high': np.array(data_df['High']),
    'low': np.array(data_df['Low']),
    'close': np.array(data_df['Close']),
    'volume': np.array(data_df['Volume'])
    }

    return inputs


def pnl_module_per_stock(buy_sig, sell_sig):
    pass
