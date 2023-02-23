# Importing the API and instantiating the REST client according to our keys
from alpaca.trading.client import TradingClient
from alpaca.trading.requests import MarketOrderRequest
from alpaca.trading.enums import OrderSide, TimeInForce
from alpaca.trading.requests import GetAssetsRequest
from config import *



trading_client = TradingClient(API_KEY, SECRET_KEY, paper=False)


# Getting account information and printing it
account = trading_client.get_account()
for property_name, value in account:
    print(f"\" {property_name}\" : {value}")


# Setting parameters for a buy order
market_order_data = MarketOrderRequest(
                    symbol = "XYZ",
                    qty = 1,
                    side = OrderSide.BUY,
                    time_in_force = TimeInForce.GTC
)

# Submitting the order and then priting the returned object
market_order = trading_client.submit_order(market_order_data)


# Viewing open positions and priting them
my_positions = trading_client.get_all_positions()

for position in my_positions:
    for property_name, value in position:
        print(f"\"{property_name}\" : {value}")



# View today's balance change
balance_change = float(account.equity) - float(account.last_equity)
print(f'Today\'s portfolio balance change: ${balance_change}')

# Bracket Order
{
  "side": "buy",
  "symbol": "SPY",
  "type": "market",
  "qty": "100",
  "time_in_force": "gtc",
  "order_class": "bracket",
  "take_profit": {
    "limit_price": "301"
  },
  "stop_loss": {
    "stop_price": "299",
    "limit_price": "298.5"
  }
}


# Trailing stop order
# Trail price is hwm - trail. Can also do trail percent
{
  "side": "sell",
  "symbol": "SPY",
  "type": "trailing_stop",
  "qty": "100",
  "time_in_force": "day",
  "trail_price": "6.15"
}