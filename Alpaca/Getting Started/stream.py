from config import *
import websocket, json

def on_open(ws):
    print("opened")

    auth_data = {
        "action": "auth",
        "params": API_KEY
    }

    ws.send(json.dumps(auth_data))

    channel_data = {
        "action": "subscribe",
        "params": TICKERS
    }

    ws.send(json.dumps(channel_data))


def on_message(ws, message):
    print("received a message")
    print(message)

def on_close(ws):
    print("closed connection")

socket = "wss://stream.data.alpaca.markets/v2/iex"

# On_open, when websocket recieves a request what do we want it to do... etc
ws = websocket.WebSocketApp(socket, on_open=on_open)
ws.run_forever()

{"action": "authenticate","data": {"key_id": API_KEY, "secret_key": SECRET_KEY}}