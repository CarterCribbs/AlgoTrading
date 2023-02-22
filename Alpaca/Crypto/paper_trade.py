from alpaca.trading.client import TradingClient
from alpaca.trading.requests import MarketOrderRequest
from alpaca.trading.enums import OrderSide, TimeInForce
from alpaca.trading.requests import GetAssetsRequest


API_KEY = "PKS35VB0DKZA6A20G7VS"
SECRET_KEY = "Y5Ql5wOTqsnaF1taulef7c8bbFmDsWvb5BRwDHcg"
APCA_API_BASE_URL= "https://paper-api.alpaca.markets"

trading_client = TradingClient(API_KEY, SECRET_KEY, paper=True)

