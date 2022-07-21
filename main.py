import pandas as pd
import numpy as np
import json
import requests
import pycoingecko as pygc

from ema_calculator import ema_calculatoor

## TODO: Get data
## cg good for historical daily data
cg = pygc.CoingGeckoAPI()

coinlist = ['eth']

timeframe = pd.date_range(start='1-1-2016',
                       end='18-7-2022',
                       freq='4H')

eth = [cg.get_coin_history_by_id('ethereum', '-'.join(str(timeframe[i]).split(' ')[0].split('-')[::-1]))['market_data']['current_price']['usd'] for i in range(len(timeframe))]

df = pd.DataFrame({'date': timeframe,
                  'price': eth})

df.set_index('date', inplace=True)

## TODO: FUTURE:: Multivariate & NLP -> more data sources

## TODO: perform analysis of data (LSTM, ema cross, etc.)
alpha = 0.167
ema6 = ema_calculatoor(eth,alpha=alpha)
        

    

## TODO: return decision

## TODO: test decision // Sum of decisions

## TODO: select successful strategy