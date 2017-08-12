#code
from zipline.api import order, record, symbol
from zipline.algorithm import TradingAlgorithm
import pytz
from datetime import datetime
import pandas as pd

# sys.path.append('.\DownloadNseData')
# import important_module

import pytz
from pandas.io.data import DataReader
from collections import OrderedDict
data = OrderedDict()
start_date = '9/17/2011'
end_date = '6/24/2015'
data['SPY'] = DataReader('SPY',data_source='google',start=start_date, end=end_date)
data['SPY'].to_csv('SPY.csv')
print (data['SPY'].head())
# type(data['SPY'])
panel = pd.Panel(data)
panel.minor_axis = ['Open', 'High', 'Low', 'Close', 'Volume']
panel.major_axis = panel.major_axis.tz_localize(pytz.utc)
data = panel

def initialize(context):
   pass

def handle_data(context, data):
  order(symbol('SPY'), 10)
  record(SPY=data.current(symbol('SPY'), 'price'))

algo_obj = TradingAlgorithm(initialize=initialize, handle_data=handle_data)
perf_manual = algo_obj.run(data)