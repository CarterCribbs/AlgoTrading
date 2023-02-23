from alpaca.trading.client import TradingClient
from alpaca.trading.requests import MarketOrderRequest
from alpaca.trading.enums import OrderSide, TimeInForce
from alpaca.trading.requests import GetAssetsRequest


API_KEY = ""
SECRET_KEY = ""
APCA_API_BASE_URL= "https://paper-api.alpaca.markets"

trading_client = TradingClient(API_KEY, SECRET_KEY, paper=True)

