# Libraries
import time

# Balance
from binance.client import Client
client = Client("Ym9Q708iiI5rf2vMsk3X22A05ljyVaxGMbC0TamYJf7TfNoX8VBmX19usZLjioHH",
                "KlFeWIVZ80uoW1MZJl5v6KneaCycVxo834QM98C9HEibhUO60nBNJIV1npQ1Hvn3")
balance = client.get_asset_balance(asset="USDT")
print(balance)

# Config
coin = "XRP"
pairing = "USDT"
quantity = 10.00


def buy_coin():
    return client.order_market_buy(
        symbol=coin+pairing,
        quantity=quantity)


def main():
    while True:
        print("BUYING XRP")
        buy_coin()
        time.sleep(10)


if __name__ == "pythonProject4":
    main()
