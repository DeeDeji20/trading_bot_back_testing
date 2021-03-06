from AlgorithmImports import *
from yahoo_reader import YahooData


class Yahoodata(QCAlgorithm):
    def Initialize(self):
        self.SetStartDate(2022, 6, 10)  # Set Start Date
        self.SetEndDate(2022, 6, 11)  # Set End Date
        self.SetCash(100000)  # Set Strategy Cash
        self.AddData(Yahoodata,"SPY", Resolution.Daily).Symbol

    def OnData(self, data):
        """OnData event is the primary entry point for your algorithm. Each new data point will be pumped in here.
            Arguments:
                data: Slice object keyed by symbol containing the stock data
        """
        if not self.Portfolio.Invested:
            self.SetHoldings("SPY", 1)
            self.Debug("Purchased Stock")
        
        self.Debug(f"{self.symbol.Value} - {self.Time}: Close={data[self.symbol].Close}")
