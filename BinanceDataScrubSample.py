from socket import socket
import websocket, json

cc = 'btcusd'
interval = '1m'

socket = f'wss://fstream.binance.com/ws/{cc}t@kline_{interval}'

closes, highs, lows = [], [], []

def on_message(ws,message):
	json_message = json.loads(message)
	candle = json_message['k']
	is_candle_closed = candle['x']
	close = candle ['c']
	high = candle['h']
	low = candle['l']
	vol = candle['v']

	if is_candle_closed:
		closes.append(float(close))
		highs.append(float(high))
		lows.append(float(low))
	print(f'"Close: "{close}')
	print(f'"High: "{high}')
	print(f'"Low: "{low}','\n')

	printThisClose = close

	#print(printThisClose)


	#print(closes)
	#print(highs)
	#print(lows)


def on_close(ws):
	print("Connection Closed")

ws = websocket.WebSocketApp(socket, on_message = on_message, on_close = on_close)

ws.run_forever()