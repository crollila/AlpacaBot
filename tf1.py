from alpaca.trading.client import TradingClient
from alpaca.trading.enums import OrderSide, TimeInForce
from alpaca.trading.requests import MarketOrderRequest, ClosePositionRequest

# Initialize Alpaca Trading Client
api_key = ''
api_secret = ''
trading_client = TradingClient(api_key, api_secret, paper=True)

def get_account_info():
    """Function to get account information."""
    account = trading_client.get_account()
    return account


def calculate_quantity(purchasing_power, price):
    """Calculate quantity based on 1% of account's purchasing power and given price."""
    amount_to_trade = purchasing_power * 0.01
    quantity = amount_to_trade / price
    return quantity


def close_all_positions(symbol):
    """Close all positions for a given symbol."""
    try:
        position = trading_client.get_open_position(symbol)
        if position:
            trading_client.close_position(symbol)
            print(f"Closed all positions for {symbol}")
    except Exception as e:
        print(f"Error closing positions for {symbol}: {e}")

def place_order(symbol, qty, side):
    """Function to place an order."""
    order_data = MarketOrderRequest(
        symbol=symbol,
        qty=qty,
        side=OrderSide.BUY if side.lower() == 'buy' else OrderSide.SELL,
        time_in_force=TimeInForce.GTC
    )

    response = trading_client.submit_order(order_data=order_data)
    return response

def execute_trade(action, symbol, price):
    try:
        account = get_account_info()
        purchasing_power = float(account.buying_power)
        print(f"Account Purchasing Power: {purchasing_power}")

        if action == 'buy':
            quantity = calculate_quantity(purchasing_power, price)
            print(f"Calculated Quantity for {symbol} at price {price}: {quantity}")
            response = place_order(symbol, quantity, action)
            print(f"Order {action} for {quantity} of {symbol} executed")
        elif action == 'sell':
            close_all_positions(symbol)  # Close all positions for the symbol
            response = "Closed all positions"  # Update response for the 'sell' action

        print(f"Alpaca API response: {response}")
    except Exception as e:
        print(f"Error executing trade: {e}")

