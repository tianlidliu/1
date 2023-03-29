from alpaca.data.live import CryptoDataStream

# 1. Instead of hardcoding these in the python file, try reading these from a file (referred to as a secrets file)
# 2. Look up the use of .gitignore and make sure that the secrets file is in the gitignore so that you don't accidentally commit it upstream
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


# 1. Look into the crypto stream API reference on alpaca and see if you can output the results to a file on your computer
# 2. (And this is a big one...) Instead of a file, see if you can get this to write into a database. We can do this one together on a conference call when you're ready for it. 
crypto_stream.run()
