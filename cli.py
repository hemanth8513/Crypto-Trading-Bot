import argparse
from dotenv import load_dotenv
import os
import logging
from bot import BasicBot

# Load API credentials from .env
load_dotenv()

# Logging setup
os.makedirs('logs', exist_ok=True)
logging.basicConfig(
    filename='logs/bot.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def main():
    parser = argparse.ArgumentParser(description="Binance Futures Testnet Trading Bot")
    parser.add_argument('--symbol', required=True, help='e.g., BTCUSDT')
    parser.add_argument('--side', required=True, choices=['buy', 'sell'])
    parser.add_argument('--quantity', type=float, required=True)
    parser.add_argument('--type', required=True, choices=['market', 'limit', 'stop_limit'])
    parser.add_argument('--price', type=float, help='Price for limit/stop-limit orders')
    parser.add_argument('--stop_price', type=float, help='Stop price for stop-limit orders')

    args = parser.parse_args()

    api_key = os.getenv("API_KEY")
    api_secret = os.getenv("API_SECRET")

    bot = BasicBot(api_key, api_secret)

    if args.type == "market":
        result = bot.place_market_order(args.symbol, args.side, args.quantity)
    elif args.type == "limit":
        if args.price is None:
            print("❌ Error: --price is required for limit orders.")
            return
        result = bot.place_limit_order(args.symbol, args.side, args.quantity, args.price)
    elif args.type == "stop_limit":
        if args.price is None or args.stop_price is None:
            print("❌ Error: --price and --stop_price are required for stop-limit orders.")
            return
        result = bot.place_stop_limit_order(args.symbol, args.side, args.quantity, args.price, args.stop_price)
    else:
        print("❌ Unsupported order type.")
        return

    if result:
        print("✅ Order placed successfully!")
        print(result)
    else:
        print("❌ Order failed. Check logs for more info.")

if __name__ == "__main__":
    main()
