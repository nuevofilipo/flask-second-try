from flask import Flask, jsonify
import os
from binance.spot import Spot as Client
import pandas as pd

app = Flask(__name__)

api_key = "LS2FxhfRjqp6TOv3q2QFOGuQzU8KoSGwlcLIOVaxjRjc0UOhncD2ZRMzT4xRGsfu"
secret_key = "p3AHHm2sq26yV2y92y0XkFkDxNqE3AAPVphtslNzrmLAJOrMN3r5Gm8ohNolfsXn"
spot_client = Client(api_key, secret_key)
columns = ["Open time", "Open", "High", "Low", "Close", "Volume", "Close time", "Quote asset volume",
              "Number of trades", "Taker buy base asset volume", "Taker buy quote asset volume", "Ignore"]



@app.route('/')
def index():
    return "hello world, luckily this application works!"


@app.route('/btcusd')
def btcusd():
    btcusd_historical = spot_client.klines("BTCUSDT", "1d", limit=1000)
    df = pd.DataFrame(btcusd_historical, columns= columns)
    return df.to_json(orient='records')


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
