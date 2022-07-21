import pandas as pd
import numpy as np
import json
import requests
import pycoingecko as pygc

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
ema_6_init = eth[0]
ema_9_init = eth[0]
def ema6_calculatoor(coin_price_list, ema = 0.0, alpha = 0.167):
    if ema == 0.0:
        ema = coin_price_list.pop(0)
        return ema6_calculatoor(coin_price_list, ema=ema)
    else:
        ema = ema + alpha * (coin_price_list.pop(0) - ema)
        if len(coin_price_list) == 0:
            return ema
        else:
            return ema6_calculatoor(coin_price_list, ema=ema)

    

## TODO: return decision

## TODO: test decision // Sum of decisions

## TODO: select successful strategy