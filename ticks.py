import yfinance as yf
import logging
import time
import os

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(message)s", datefmt="%d-%b-%y %H:%M:%S"
)

last_price_dict = {}


class Ticks:
    def __init__(self):
        self.tickers = None

    def start_ticker(self, ticker_strings):
        self.tickers = [yf.Ticker(a) for a in ticker_strings]
        for each_tick in self.tickers:
            # get the last price data.
            last_price = each_tick.fast_info.last_price
            symbol = "?"
            try:
                if last_price > last_price_dict[each_tick.ticker]:
                    symbol = "+"
                else:
                    symbol = "-"
            except:
                pass
            finally:
                last_price_dict[each_tick.ticker] = last_price

            b = f"=== {each_tick.ticker} {last_price} {symbol}"
            logging.info(b)


def looping():
    t = Ticks()
    t.start_ticker(["EURUSD=X", "SI=F", "WAVES-EUR"])
    time.sleep(50)
    os.system("cls")


if __name__ == "__main__":
    while True:
        looping()
