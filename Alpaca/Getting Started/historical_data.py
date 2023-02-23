from alpaca.data.historical import CryptoHistoricalDataClient
from alpaca.data.timeframe import TimeFrame

client = CryptoHistoricalDataClient()

# Creating request 
request_params = CryptoBarsRequest(
                        symbol_or_symbols=["BTC/USD"],
                        timeframe=TimeFrame.Day,
                        start="2022-09-01",
                        end="2022-09-07"
                        )

# Retrieve daily bars for Bitcoin in a DF and priting it
btc_bars = client.get_crypto_bars(request_params)

# Convert to DF
btc_bars.df

print(btc_bars)