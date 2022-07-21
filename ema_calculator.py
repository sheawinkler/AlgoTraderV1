def ema_calculatoor(coin_price_list, ema = 0.0, alpha = 0.167, return_list = []):
    ## alpha is defined as 1 / n, where n is the number of time steps to include in the ema
    #### default will be n=6.
    if ema == 0.0:
        ema = coin_price_list.pop(0)
        return_list.append(ema)
        return ema_calculatoor(coin_price_list, ema=ema, return_list=return_list)
    else:
        ema = ema + alpha * (coin_price_list.pop(0) - ema)
        return_list.append(ema)
        if len(coin_price_list) == 0:
            return return_list
        else:
            return ema_calculatoor(coin_price_list, ema=ema, return_list=return_list)