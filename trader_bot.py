
import numpy as np
from binance import Client

class traderbot():

    def __init__(self):
        api_key = "GCswSd13dQUyfUrxmwH0TQvMUxv9SXWR3AEaL8yuMI9VYXgYNZtWmKo42mFLEaZc"
        apt_sec = "QmfCSucR9TxDefDIWG9yDF7SXjxMC1kr3UvcDrHUOzJ0RT8tAMmhMdpHM1fOFhsi"
        client = Client(api_key, apt_sec, tld='us')
