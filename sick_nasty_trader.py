# Code to do some sick nasty HFT


import numpy as np
from binance import Client, ThreadedWebsocketManager, ThreadedDepthCacheManager



# Model stock market movement as a mass-spring-dampener system on a moving base.
# Apply ML/AI techniques to find suitable coefficients of the mass spring dampener.
# Possibly have some sort of volume (trading, issued, etc.) as mass?
print('------------------------------------------')
api_key = str("Xz5FMQ1Sdena0pN223ZsjL5eMRbslgbkMLAj8wz5CeKLSXJOGpQHxnziVSwIKFzN")
apt_sec = str("W5Em8CrGyLF1vnQBzXg1mjCz9n33GZoHtOBbjlk6sxkINaoHjkCL4AVo4akXuhHk")
client = Client(api_key, apt_sec)

# get market depth
depth = client.get_order_book(symbol='BNBBTC')


# get all symbol prices
lrcprice = client.get_symbol_ticker(symbol='LRCUSDT')
print(lrcprice)




