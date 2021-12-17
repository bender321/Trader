from trader import Trader


class TestTrader:

    def test_on_trade(self):
        trader = Trader()
        trader.on_trade(int(1618462800.0), 30, 10.34)
        trader.on_trade(int(1618462800.2), 50, 10.34)
        trader.on_trade(int(1618462800.3), 10, 10.36)
        trader.on_trade(int(1618462800.3), 60, 10.35)
        trader.on_trade(int(1618462800.5), 12, 10.34)

        assert len(trader._data) != 0

    def test_get_sum(self):
        trader = Trader()
        trader.on_trade(int(1618462800.0), 30, 10.34)
        trader.on_trade(int(1618462800.2), 50, 10.34)
        trader.on_trade(int(1618462800.3), 10, 10.36)
        trader.on_trade(int(1618462800.3), 60, 10.35)
        trader.on_trade(int(1618462800.5), 12, 10.34)

        assert trader.get_sum() == 0
