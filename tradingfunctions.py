from alpaca.trading.client import TradingClient
from alpaca.trading.enums import OrderSide, TimeInForce
from alpaca.trading.requests import MarketOrderRequest

# Initialize Alpaca Trading Client
api_key = ''
api_secret = ''
trading_client = TradingClient(api_key, api_secret, paper=True)

def get_account_info():
    """Function to get account information."""
    account = trading_client.get_account()
    return account

def place_order(symbol, qty, side):
    """Function to place an order."""
    order_data = MarketOrderRequest(
        symbol=symbol,
        qty=qty,
        side=OrderSide.BUY if side.lower() == 'buy' else OrderSide.SELL,
        time_in_force=TimeInForce.GTC  # Adjusted TimeInForce
    )

    response = trading_client.submit_order(order_data=order_data)
    return response

def execute_trade(action, symbol, quantity):
    """Function to execute a trade based on TradingView alert."""
    try:
        response = place_order(symbol, quantity, action)
        print(f"Order {action} for {quantity} of {symbol} executed")
        print(f"Alpaca API response: {response}")

        # Additional logging
        if response:
            print(f"Order response: {response}")
            # Uncomment these if needed, based on the response structure
            # print(f"Order status: {response.status}")
            # if response.status == 'rejected':
            #     print(f"Order rejected reason: {response.rejected_reason}")
    except Exception as e:
        print(f"Error executing trade: {e}")
