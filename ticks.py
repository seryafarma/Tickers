import yfinance as yf
import time
import os
from tabulate import tabulate

last_price_dict = {}


class Ticks:
    def __init__(self):
        self.tickers = None
        self.display = []

    def start_ticker(self, ticker_strings):
        current_time = time.strftime("%Y-%m-%d %H:%M")
        self.display = []

        self.tickers = [yf.Ticker(a) for a in ticker_strings]
        for each_tick in self.tickers:
            lst = []
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

            lst.append(current_time)
            lst.append(each_tick.ticker)
            lst.append(last_price)
            lst.append(symbol)

            self.display.append(lst)

    def get_display(self):
        return self.display


def looping():
    t = Ticks()
    t.start_ticker(["EURUSD=X", "SI=F", "WAVES-EUR"])

    print(tabulate(t.get_display(), tablefmt="grid"))
    time.sleep(50)
    os.system("cls")


if __name__ == "__main__":
    while True:
        looping()
