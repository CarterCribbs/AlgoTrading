import alpaca_trade_api as tradeapi 
import threading


# authentication and connection
api_key = 'insert api'
api_secret = 'insert api secret'
base_url = 'httsps://paper-api.alpaca.markets' #check to make sure this is correct
data_url = 'wss://data.alpaca.markets'


# instantiate REST API
api = tradeapi.REST(api_key, api_secret, base_url, api_version='v2')

# print account information
account = api.get_account()
print(account)



# get data
# valid time intervals are 1Min, 5Min, 15Min and 1D
appl = api.gt_barset('AAPL', '1Min')



# Use WebSockets to push info wihtout making constant request
# calls to the API

ws_url = 'wss://data.alpaca.markets'

conn = tradeapi.stream2.SteramConn(api_key, api_secret, base_url, data_url=ws_url, data_stream=
alpacadatav1')



# async def is a coroutine function - function that can be suspended and resumed

@conn.on(r'^account_updates$')
async def on_account_updates(conn, channel, account): 
    print('account', account)

@conn.on(r'^trade_updates$')
async def on_trade_updates(conn, channel, trade):
    print('trade', trade)

def ws_start():
    conn.run(['account_updates', 'trade_udpates'])

# start WebSocket in a thread
ws_thread = threading.Thread(target=ws_start, daemon=True)
ws_thread.start()




# submitting an order 
api.submit_order(symbol = __ , qty= __ , side = __ , time_in_force = 'gtc', type = 'limit', limit_price = __, client_order_id__

# stop loss and take profit, this is all enclsoed in the submit_order
stop_loss = dict(sop_price = __)
take_profit = dict(limit_price = __))


# get position
poistion = api.get_position('TSLA')

# to check if you can trade a stock, include a try/execpt block in case not found
aapl_asset = api.get_asset('AAPL')

