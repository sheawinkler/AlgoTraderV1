import pandas as pd
import numpy as np
import json
import requests
import pycoingecko as pygc

from ema_calculator import ema_calculatoor
from coingecko import get_CGcoin_data

## TODO: Get data
## cg good for historical daily data
cg = pygc.CoingGeckoAPI()

coinlist = ['ethereum']


begin_date = '1-1-2016'
end_date = '20-7-2022'
freq = '4H'


eth = get_CGcoin_data(begin_date,end_date,freq,'ethereum')

df = pd.DataFrame({'date': timeframe,
                  'price': eth})

df.set_index('date', inplace=True)

## TODO: FUTURE:: Multivariate & NLP -> more data sources

## TODO: perform analysis of data (ema cross -> LSTM -> beyond, etc.)
alpha6 = np.divide(1,6)
ema6 = ema_calculatoor(eth,alpha=alpha6)

alpha9 = np.divide(1,9)
ema9 = ema_calculatoor(eth,alpha=alpha9)

## TODO: return decision    
flag = 0
longest_ema = 9
decisions = []
    
for i,j in zip(ema6,ema9):
    if longest_ema > 0:
        longest_ema = longest_ema - 1
        continue
    if i > j and flag == 0:
        print('ema6 crosses above ema9 - buy')
        decisions.append('Buy')
        flag = 1
    if i > j and flag == 1:
        print('hold')
    if i < j and flag == 0:
        print('ema6 crosses below ema9 - sell')
        flag == 1
        decisions.append('Sell')
    if i < j and flag == 0:
        print('patience is a virtue or you can yolo')
    

## TODO: test decision // Sum of decisions
## TODO: logic: conservative_decison = if high_price_at_purchase > low_price_at_sell then true
## ## ## now only getting daily close price so will have to alter API call for functionality
## TODO: FIRST, let's make a decision model that can chart it's decisions



## TODO: select successful strategy