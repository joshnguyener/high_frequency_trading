# Code to do some sick nasty HFT


import numpy as np
from binance import Client, ThreadedWebsocketManager, ThreadedDepthCacheManager
import csv
import time


# Model stock market movement as a mass-spring-dampener system on a moving base.
# Apply ML/AI techniques to find suitable coefficients of the mass spring dampener.
# Possibly have some sort of volume (trading, issued, etc.) as mass?
print('------------------------------------------')
api_key = "GCswSd13dQUyfUrxmwH0TQvMUxv9SXWR3AEaL8yuMI9VYXgYNZtWmKo42mFLEaZc"
apt_sec = "QmfCSucR9TxDefDIWG9yDF7SXjxMC1kr3UvcDrHUOzJ0RT8tAMmhMdpHM1fOFhsi"
client = Client(api_key, apt_sec, tld='us')

# get all symbol prices
lrcprice = client.get_symbol_ticker(symbol='LRCUSDT')
user = client.get_account()


while True:
    trades = client.get_recent_trades(symbol='LRCUSD')
    avg_price = client.get_avg_price(symbol='LRCUSD')
    lrcprice = client.get_symbol_ticker(symbol='LRCUSD')
    print(trades[499])
    time.sleep(5)