
import numpy as np
from binance import Client
import csv
import time
import threading
from datetime import datetime

class Price_Recorder():

    def __init__(self):
        api_key = "GCswSd13dQUyfUrxmwH0TQvMUxv9SXWR3AEaL8yuMI9VYXgYNZtWmKo42mFLEaZc"
        apt_sec = "QmfCSucR9TxDefDIWG9yDF7SXjxMC1kr3UvcDrHUOzJ0RT8tAMmhMdpHM1fOFhsi"
        self.client = Client(api_key, apt_sec, tld='us')

    def begin_price_recording(self, coin_symbol = "BTCUSDT"):
        headersCSV = ['symbol','price','time', 'date']
        while True:
            with open("C:/Users/jngu114/OneDrive - Louisiana State University/8. Personal/Stock_Price_History/eth_price_histroy.csv", 'a', newline='') as f:
                lrcprice = self.client.get_symbol_ticker(symbol=coin_symbol)
                dictwriter_object = csv.DictWriter(f, fieldnames=headersCSV)
                lrcprice['time'] = time.time()
                now = datetime.now()
                lrcprice['date'] = now.strftime('%b-%d-%Y %H:%M:%S')
                dictwriter_object.writerow(lrcprice)
                print(lrcprice)
                time.sleep(5)

    def start(self, coin_symbol = "BTCUSDT"):
        thread = threading.Thread(target=self.begin_price_recording, kwargs={'coin_symbol': coin_symbol})
        thread.daemon = True
        thread.start()
                

if __name__ == '__main__':
    obj = Price_Recorder()
    obj.start(coin_symbol='ETHUSD')
    while (1):
        pass