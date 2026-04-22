import argparse
import logging
from bot.client import BinanceClient
from bot.orders import place_order
from bot.validators import (
    validate_side,
    validate_order_type,
    validate_quantity,
    validate_price,
    validate_stop_price
)
from bot.logging_config import setup_logger


def main():
    setup_logger()

    parser = argparse.ArgumentParser(description="Binance Futures Trading Bot")

    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True)
    parser.add_argument("--type", required=True)
    parser.add_argument("--quantity", type=float, required=True)
    parser.add_argument("--price", type=float)
    parser.add_argument("--stop_price", type=float)

    args = parser.parse_args()

    try:
        # Validation
        validate_side(args.side)
        validate_order_type(args.type)
        validate_quantity(args.quantity)
        validate_price(args.price, args.type)
        validate_stop_price(args.stop_price, args.type)

        client = BinanceClient()

        # Market price
        price_info = client.get_mark_price(args.symbol)
        market_price = float(price_info['markPrice'])

        print("\n========== MARKET INFO ==========")
        print(f"Symbol        : {args.symbol}")
        print(f"Market Price  : {market_price}")
        print("=================================")

        # Minimum Notional Check (IMPORTANT)
        notional = market_price * args.quantity
        if notional < 100:
            raise ValueError(f"Order value must be at least 100 USDT. Current: {notional:.2f}")

        # LIMIT validation
        if args.type == "LIMIT":
            if args.side == "SELL" and args.price < market_price:
                raise ValueError("SELL price must be >= market price")
            if args.side == "BUY" and args.price > market_price:
                raise ValueError("BUY price must be <= market price")

        # STOP validation
        if args.type == "STOP":
            if args.side == "SELL" and args.stop_price < market_price:
                print("⚠️ Warning: Stop price below market may trigger immediately")
            if args.side == "BUY" and args.stop_price > market_price:
                print("⚠️ Warning: Stop price above market may trigger immediately")

        # Summary
        print("\n========== ORDER SUMMARY ==========")
        print(f"Symbol        : {args.symbol}")
        print(f"Side          : {args.side}")
        print(f"Order Type    : {args.type}")
        print(f"Quantity      : {args.quantity}")
        print(f"Notional      : {notional:.2f} USDT")
        if args.price:
            print(f"Price         : {args.price}")
        if args.stop_price:
            print(f"Stop Price    : {args.stop_price}")
        print("===================================")

        # Place order
        response = place_order(
            client,
            args.symbol,
            args.side,
            args.type,
            args.quantity,
            args.price,
            args.stop_price
        )

        # Response
        print("\n========== ORDER RESPONSE ==========")
        print(f"Order ID      : {response.get('orderId')}")
        print(f"Status        : {response.get('status')}")
        print(f"Executed Qty  : {response.get('executedQty')}")
        print(f"Avg Price     : {response.get('avgPrice', 'N/A')}")
        print("===================================")

        if response.get("status") == "FILLED":
            print("\n✅ Order executed successfully!")
        else:
            print("\n⏳ Order placed successfully and waiting to be filled.")

    except Exception as e:
        logging.error(f"CLI Error: {str(e)}")
        print(f"\n❌ Error: {str(e)}")


if __name__ == "__main__":
    main()