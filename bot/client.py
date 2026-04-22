import os
from binance.client import Client
from dotenv import load_dotenv
import logging

load_dotenv()

class BinanceClient:
    def __init__(self):
        api_key = os.getenv("API_KEY")
        api_secret = os.getenv("API_SECRET")

        if not api_key or not api_secret:
            raise ValueError("API_KEY or API_SECRET not found in .env file")

        self.client = Client(api_key, api_secret)

        # Futures Testnet
        self.client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"

    def place_order(self, **params):
        try:
            logging.info(f"API Request: {params}")
            response = self.client.futures_create_order(**params)
            logging.info(f"API Response: {response}")
            return response
        except Exception as e:
            logging.error(f"API Error: {str(e)}")
            raise

    def get_mark_price(self, symbol):
        return self.client.futures_mark_price(symbol=symbol)

    def get_balance(self):
        return self.client.futures_account_balance()

    def get_order(self, symbol, order_id):
        return self.client.futures_get_order(symbol=symbol, orderId=order_id)