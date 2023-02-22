from config import *
from alpaca.trading.client import TradingClient
from alpaca.trading.requests import MarketOrderRequest
from alpaca.trading.enums import OrderSide, TimeInForce




trading_client = TradingClient(API_KEY, SECRET_KEY, paper = True)

# Getting account information and printing it
account = trading_client.get_account()
for property_name, value in account:
  print(f"\"{property_name}\": {value}")



# Setting parameters for our buy order
market_order_data = MarketOrderRequest(
                      symbol="BTC/USD",
                      qty=0.1,
                      side=OrderSide.BUY,
                      time_in_force=TimeInForce.GTC
                  )


# Submitting the order and then printing the returned object
market_order = trading_client.submit_order(market_order_data)
for property_name, value in market_order:
  print(f"\"{property_name}\": {value}")