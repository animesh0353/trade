from datetime import date
import pandas_datareader as pdr
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import talib
import os
import time


def google_portfolio_conveter():
    '''
    module to create symbol list from google portfolio
    :return: None
    '''
    data_df = pd.read_csv('portfolio.csv', sep=',', header=0, index_col=1)
    f = open('symbol_list.csv', 'w')
    for index in data_df.index:
        f.write(index + '.NS' + "\n")
    f.close()


# main function
if __name__ == "__main__":

    start_time = time.time()
    s1 = date(2010,1,1)
    e1 = date.today() #date(2017,8,1)
    # symb = 'SBIN.NS'

    dir = r'./csvData'
    f = open('symbol_list.csv', 'r')
    counter = 0

    # to read the symbol from symbol_list.csv file
    for line in f:
        symb = line.strip('\n')
        symb_file = os.path.join(dir, symb+'.csv')

        # if file exits then append the file with new OHLCV data else create the file
        if os.path.isfile(symb_file):
            data_df = pd.read_csv(symb_file, sep=',', header=0, index_col=0, parse_dates=['Date'])
            prev_data = data_df.index[-1]
            data_df_append = pdr.get_data_yahoo(symbols=symb, start=prev_data, end=date.today())
            for index, row in data_df_append.iterrows():
                data_df.loc[index] = row

        # download the data from 2010 till today
        else:
            data_df = pdr.get_data_yahoo(symbols=symb, start=s1, end=date.today())

        # save the DataFrame
        data_df.to_csv(symb_file)
        counter += 1
        if counter % 10 == 0:
            print ("Completed for " + str(counter) + " symbol")

    # calculate time
    end_time = time.time()
    print (end_time-start_time, " seconds")
