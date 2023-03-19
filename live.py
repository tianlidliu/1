from alpaca.data.live import CryptoDataStream
API_KEY = ""
SECRET_KEY = ""

# Initiate class
crypto_stream = CryptoDataStream(API_KEY, SECRET_KEY)
async def bar_callback(bar):
    for property_name, value in bar:
        print(f"\"{property_name}\": {value}")

# Subscribing to bar event 
symbol = "BTC/USD"
crypto_stream.subscribe_bars(bar_callback, symbol)

crypto_stream.run()