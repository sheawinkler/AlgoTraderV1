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


## find data source for real-time crypto data

## get data into json format

## TODO: Clean data

## TODO: perform analysis of data

## TODO: return decision

## TODO: test decision // Sum of decisions

## TODO: select successful strategy