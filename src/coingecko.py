import pycoingecko as cg
import pandas as pd

def get_CGcoin_data(begin_date, end_date, freq, coin):
    timeframe = pd.date_range(start=begin_date,
                       end=end_date, 
                       freq=freq)
    coin_data = [cg.get_coin_history_by_id(coin, '-'.join(str(timeframe[i]).split(' ')[0].split('-')[::-1]))['market_data']['current_price']['usd'] for i in range(len(timeframe))]
    return coin_data