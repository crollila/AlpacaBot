from flask import Flask, request
import json
from tf1 import execute_trade

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    print("Webhook hit received")
    data = request.data.decode('utf-8')
    print("Webhook received:", data)

    try:
        alert_data = json.loads(data)
        action = alert_data['Action'].lower()
        symbol = alert_data['Ticker']
        price = float(alert_data['Price'])  # Convert price to float

        execute_trade(action, symbol, price)  # Pass price to execute_trade
    except Exception as e:
        print(f"Error parsing webhook data: {e}")
        return "Error in webhook", 500

    return "Webhook processed", 200

if __name__ == '__main__':
    app.run(port=5000)
