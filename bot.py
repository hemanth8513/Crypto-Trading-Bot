from binance.client import Client
from binance.enums import *
import logging

class BasicBot:
    def __init__(self, api_key, api_secret, testnet=True):
        self.client = Client(api_key, api_secret)
        if testnet:
            # Set Binance Futures Testnet API URL
            self.client.FUTURES_API_URL = 'https://testnet.binancefuture.com/fapi'
        logging.info("Bot initialized")

    def place_market_order(self, symbol, side, quantity):
        try:
            order = self.client.futures_create_order(
                symbol=symbol,
                side=SIDE_BUY if side.lower() == "buy" else SIDE_SELL,
                type=ORDER_TYPE_MARKET,
                quantity=quantity
            )
            logging.info(f"Market order placed: {order}")
            return order
        except Exception as e:
            logging.error(f"Market order error: {e}")
            return None

    def place_limit_order(self, symbol, side, quantity, price):
        try:
            order = self.client.futures_create_order(
                symbol=symbol,
                side=SIDE_BUY if side.lower() == "buy" else SIDE_SELL,
                type=ORDER_TYPE_LIMIT,
                timeInForce=TIME_IN_FORCE_GTC,
                quantity=quantity,
                price=price
            )
            logging.info(f"Limit order placed: {order}")
            return order
        except Exception as e:
            logging.error(f"Limit order error: {e}")
            return None

    def place_stop_limit_order(self, symbol, side, quantity, price, stop_price):
        try:
            order = self.client.futures_create_order(
                symbol=symbol,
                side=SIDE_BUY if side.lower() == "buy" else SIDE_SELL,
                type=ORDER_TYPE_STOP,
                timeInForce=TIME_IN_FORCE_GTC,
                quantity=quantity,
                price=price,
                stopPrice=stop_price
            )
            logging.info(f"Stop-limit order placed: {order}")
            return order
        except Exception as e:
            logging.error(f"Stop-limit order error: {e}")
            return None
