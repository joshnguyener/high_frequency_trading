# Class that holds various trading algorithms that will be tested and compared


import numpy as np
from binance import Client, ThreadedWebsocketManager, ThreadedDepthCacheManager
import csv
import time
import threading

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

# Algorithm Idea #1:
# Look at stock price time derivatives of varying frequencies and trade against that information
# Look at derivatives at the following times: (1, 5, 10, 30) minutes. (Apply ML alogirthm to find best derivative times)
# Checks to see if varying time derivatives are positive and negative, create conditions depending on which is 

class derivative_trader():

    def __init__(self):
        # Connect to Binance API
        api_key = "GCswSd13dQUyfUrxmwH0TQvMUxv9SXWR3AEaL8yuMI9VYXgYNZtWmKo42mFLEaZc"
        apt_sec = "QmfCSucR9TxDefDIWG9yDF7SXjxMC1kr3UvcDrHUOzJ0RT8tAMmhMdpHM1fOFhsi"
        self.client = Client(api_key, apt_sec, tld='us')
        self.deriv_flags = []
        self.signal = "Waiting...."


    def get_derivative(self,deriv_timing,csv_file = 'price_history/lrc_price_history.csv'):
        # Takes a look at the current price and the price X seconds ago and returns a derivative
        # Deriv timing should be seconds
        data_points_to_pull = int(deriv_timing/5) # We get price data every 5 seconds
        lastest_prices = self.get_price_data(data_points_to_pull, csv_file)
        derivative = (lastest_prices[0]-lastest_prices[-1])/deriv_timing
        return derivative


    def get_price_data(self,data_points = 500, csv_file = 'price_history/lrc_price_history.csv'):
        # Reads from list that stores data 
        latest_prices = []
        with open(csv_file, newline='', encoding='utf-8') as f:
            datalist = f.readlines()[-(data_points+1):]
            for ii in range(data_points):
                latest_prices.append(float(datalist[ii-1][7:15]))
            return latest_prices
            
    def if_positive(self,value):
        if value > 0:
            flag = 1
        elif value == 0:
            flag = 0
        else:
            flag = -1
        return flag

    def get_all_derivatives(self):
        # Gets derivative of price w.r.t a time. Creates a flag array if derivative is positive of not.
        while True:
            self.ten_sec_derivative = self.get_derivative(10,'price_history/eth_price_histroy.csv')
            self.one_min_derivative = self.get_derivative(60,'price_history/eth_price_histroy.csv')
            self.three_min_derivative = self.get_derivative(60*3,'price_history/eth_price_histroy.csv')
            self.five_min_derivative = self.get_derivative(60*5,'price_history/eth_price_histroy.csv')
            self.ten_min_derivative = self.get_derivative(60*10,'price_history/eth_price_histroy.csv')

            ten_sec_flag = self.if_positive(self.ten_sec_derivative)
            one_min_flag = self.if_positive(self.one_min_derivative)
            three_min_flag = self.if_positive(self.three_min_derivative)
            five_min_flag = self.if_positive(self.five_min_derivative)
            ten_min_flag= self.if_positive(self.ten_min_derivative)

            self.deriv_flags = [ten_sec_flag, one_min_flag, three_min_flag, five_min_flag, ten_min_flag]
            time.sleep(10)



    def trade_signaler_v1(self):
        # The algorithm!
        # Take a look at the derivative of the price at certain time intervals and make a decision on how to trade
        # TODO: Look at various flag combinations to determine how to trade
        # TODO: Version 1 Trader will buy when short timed derivatives are positive and long timed derivatives are negative
        # Trades when one & three minute derivative flags are positive and sell when short flags are negative and long flags are positive. Maybe sign of of uprise?
        if self.deriv_flags == [1, 1, 1, -1, -1]:
            self.signal = "BUY"
        if self.deriv_flags == [-1, 1, 1, -1, -1]:
            self.signal = "BUY"
        if self.deriv_flags == [0, 1, 1, -1, -1]:
            self.signal = "BUY"

        if self.deriv_flags == [0, 1, 1, 1, 1]:
            self.signal = "BUY"
        if self.deriv_flags == [0, 1, 1, -1, 1]:
            self.signal = "BUY"
        if self.deriv_flags == [0, 1, 1, 1, -1]:
            self.signal = "BUY"
        if self.deriv_flags == [1, 1, 1, 1, 1]:
            self.signal = "BUY"
        if self.deriv_flags == [1, 1, 1, -1, 1]:
            self.signal = "BUY"
        if self.deriv_flags == [1, 1, 1, 1, -1]:
            self.signal = "BUY"
        if self.deriv_flags == [-1, 1, 1, 1, 1]:
            self.signal = "BUY"
        if self.deriv_flags == [-1, 1, 1, -1, 1]:
            self.signal = "BUY"
        if self.deriv_flags == [-1, 1, 1, 1, -1]:
            self.signal = "BUY"

        if self.deriv_flags == [1, -1, -1, 1, 1]:
            self.signal = "SELL"
        if self.deriv_flags == [-1, -1, -1, 1, 1]:
            self.signal = "SELL"
        if self.deriv_flags == [0, -1, -1, 1, 1]:
            self.signal = "SELL"
        return self.signal



    def start(self):
        thread1 = threading.Thread(target=self.get_all_derivatives)
        thread1.daemon = True
        thread1.start()
        pass


if __name__ == '__main__':
    obj = derivative_trader()
    obj.start()
    while True:
        try:
            print(obj.deriv_flags)
            print(obj.trade_signaler_v1())
            time.sleep(5)
        except KeyboardInterrupt:
            print ('KeyboardInterrupt exception is caught')
            break



