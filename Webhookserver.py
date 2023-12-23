from flask import Flask, request
import json
from tradingfunctions import execute_trade

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    print("Webhook hit received")
    data = request.data.decode('utf-8')
    print("Webhook received:", data)

    try:
        alert_data = json.loads(data)
        action = alert_data['Action'].lower()
        quantity = float(alert_data['Contracts'])
        symbol = alert_data['Ticker']

        execute_trade(action, symbol, quantity)
    except Exception as e:
        print(f"Error parsing webhook data: {e}")
        return "Error in webhook", 500

    return "Webhook processed", 200

if __name__ == '__main__':
    app.run(port=5000)
