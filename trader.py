import datetime
import time


class Trader:

    def __init__(self, past_lookup: int = 30):
        self._data = []
        self.past_lookup = past_lookup

    def on_trade(self, timestamp: int, quantity: int, price: float) -> None:
        item = {'timestamp': timestamp, 'quantity': quantity}
        self._data.append(item)
        relevenat_time = timestamp - self.past_lookup

        for item in list(self._data):
            if item['timestamp'] < relevenat_time:
                self._data.remove(item)

    def get_sum(self) -> int:
        time_now = datetime.datetime.now()
        time_now_unix = time.mktime(time_now.timetuple())
        past_time_unix = time_now_unix - self.past_lookup
        res = 0

        for item in self._data:
            if item['timestamp'] >= past_time_unix:
                res = res + item['quantity']
            else:
                break

        return res


def main():

    mytrader = Trader()
    mytrader.on_trade(int(1618462800.0), 30, 10.34)
    mytrader.on_trade(int(1618462800.2), 50, 10.34)
    mytrader.on_trade(int(1618462800.3), 10, 10.36)
    mytrader.on_trade(int(1618462800.3), 60, 10.35)
    mytrader.on_trade(int(1618462800.5), 12, 10.34)

    print(mytrader.get_sum())


if __name__ == "__main__":
    main()
