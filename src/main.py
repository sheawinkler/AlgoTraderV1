import pandas as pd
import numpy as np
import json
import requests
import pycoingecko as pygc

from ema_calculator import ema_calculatoor
from coingecko import get_CGcoin_data

## TODO: Get data
## cg good for historical daily data

coinlist = ['ethereum']


begin_date = '1-7-2022'
end_date = '22-7-2022'
freq = '1D'

eth,timeframe = get_CGcoin_data(begin_date,end_date,freq,'ethereum')

## TODO: 
# ## need to do more with databases to store 
# ## information about coins once retrieved and not try to retrieve again

df = pd.DataFrame({'date': timeframe,
                  'price': eth})

df.set_index('date', inplace=True)
print(df.head())

## TODO: FUTURE:: Multivariate & NLP -> more data sources

## TODO: perform analysis of data (ema cross -> LSTM -> beyond, etc.)
_eth = eth.copy()
alpha6 = np.divide(1,6)
ema6 = ema_calculatoor(_eth,alpha=alpha6)

_eth = eth.copy()
alpha9 = np.divide(1,9)
ema9 = ema_calculatoor(_eth,alpha=alpha9)

#print(f'ema6: {ema6}')
#print(f'ema9: {ema9}')

## TODO: return decision    
flag = 0
eth_idx = 0
longest_ema = 9
decisions = []
prices = []

for i,j in zip(ema6,ema9):
    
    # if longest_ema > 0:
    #     longest_ema = longest_ema - 1
    #     eth_idx += 1
    #     continue
    if i > j and flag == 0:
        print('ema6 crosses above ema9 - buy')
        decisions.append('Buy')
        prices.append(eth[eth_idx])
        eth_idx += 1
        flag = 1
        continue
    if i > j and flag == 1:
        eth_idx += 1
        continue
        # print('hold')
    if i < j and flag == 0:
        print('ema6 crosses below ema9 - sell')
        flag == 1
        decisions.append('Sell')
        eth_idx += 1
        prices.append(eth[eth_idx])
    if i < j and flag == 1:
        continue
        # print('wait')
    
print(decisions)
print(prices)
## TODO: test decision // Sum of decisions
## TODO: logic: conservative_decison = if high_price_at_purchase > low_price_at_sell then true
## ## ## now only getting daily close price so will have to alter API call for functionality
## ## may need some kind of initial threshold to trigger a decision or just need lots more data than coingecko allows
## TODO: FIRST, let's make a decision model that can chart it's decisions



## TODO: select successful strategy