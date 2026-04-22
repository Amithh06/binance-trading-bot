import logging

def place_order(client, symbol, side, order_type, quantity, price=None, stop_price=None):
    try:
        params = {
            "symbol": symbol,
            "side": side,
            "quantity": quantity
        }

        if order_type == "MARKET":
            params["type"] = "MARKET"

        elif order_type == "LIMIT":
            params["type"] = "LIMIT"
            params["price"] = price
            params["timeInForce"] = "GTC"

        elif order_type == "STOP":
            # Stop-Limit Order
            params["type"] = "STOP"
            params["price"] = price
            params["stopPrice"] = stop_price
            params["timeInForce"] = "GTC"

        logging.info(f"Request: {params}")

        response = client.place_order(**params)

        logging.info(f"Response: {response}")

        return response

    except Exception as e:
        logging.error(f"Error placing order: {str(e)}")
        raise