from nsepy import get_history
from datetime import date
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import talib

s1 = date(2016,5,1)
e1 = date(2017,8,1)
symb = 'UNIPLY'


data = get_history(symbol=symb, start=s1, end=e1)
data.to_csv(symb+'.csv')

plt.plot(data[['Close']])
plt.ylabel('price')
plt.show()

close = data['Close']
c = np.array(close)
output = talib.SMA(c)

plt.plot(data[['Close']])
plt.plot(close.index, output)
plt.ylabel('price')
plt.show()

stk_sma = pd.DataFrame(output, columns=['Close'],index=close.index)

sma = data[['Close']] - stk_sma


#for index, row in sma.iterrows():