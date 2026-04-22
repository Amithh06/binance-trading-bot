def validate_side(side):
    if side not in ["BUY", "SELL"]:
        raise ValueError("Side must be BUY or SELL")

def validate_order_type(order_type):
    if order_type not in ["MARKET", "LIMIT", "STOP"]:
        raise ValueError("Order type must be MARKET, LIMIT, or STOP")

def validate_quantity(qty):
    if qty <= 0:
        raise ValueError("Quantity must be positive")

def validate_price(price, order_type):
    if order_type in ["LIMIT", "STOP"] and (price is None or price <= 0):
        raise ValueError("LIMIT/STOP orders require a valid price")

def validate_stop_price(stop_price, order_type):
    if order_type == "STOP":
        if stop_price is None or stop_price <= 0:
            raise ValueError("STOP order requires a valid stop price")