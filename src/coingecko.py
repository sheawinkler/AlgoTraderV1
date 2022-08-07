import pycoingecko as cg
import pandas as pd
import time

cg = cg.CoinGeckoAPI()

def get_CGcoin_data(begin_date, end_date, freq, coin):
    timeframe = pd.date_range(start=begin_date,
                       end=end_date, 
                       freq=freq)
    coin_data_list = []
    for i in range(len(timeframe)):
        print('check # {}'.format(i))
        coin_data_list.append(cg.get_coin_history_by_id(coin,
                                '-'.join(str(timeframe[i]).split(' ')[0].split('-')[::-1]))['market_data']['current_price']['usd'] )
        #print(coin_data_list)
        time.sleep(1.3)
    # coin_data = [cg.get_coin_history_by_id(coin, 
    #                 '-'.join(str(timeframe[i]).split(' ')[0].split('-')[::-1]))['market_data']['current_price']['usd'] 
    #              for i in range(len(timeframe))
    #              if time.sleep(1.1) is None]
    return coin_data_list,timeframe