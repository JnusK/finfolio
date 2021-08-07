# 1st 5 candles will form a band which is the highest high and lowest low
# 2nd 5 candles need to  have at least 1 candle exceed the highest high and lowest low each with the last breakout showing the direction
# use in conjunction with other indicators like RSI
# https://www.investopedia.com/investing/market-reversals-and-how-spot-them/
# https://buertrades.blogspot.com/2018/05/how-to-use-sushi-roll-in-technical-analysis.html
import pandas as pd

from main.util.enums import Trend


class SushiRoll:
    def __init__(self, data: pd.DataFrame):
        self.trend = {}
        date = data.index
        for index in range(len(date)):
            if index < 9:
                self.trend[date[index]] = Trend.UNKNOWN
            else:
                highest = data['high'][index - 9: index - 4].max()
                lowest = data['low'][index - 9: index - 4].max()
                highest_sub = data['high'][index - 4: index + 1].max()
                lowest_sub = data['low'][index - 4: index + 1].min()
                if highest_sub > highest and lowest_sub < lowest:
                    self.trend[date[index]] = Trend.BREAKOUT
                else:
                    self.trend[date[index]] = Trend.UNKNOWN

    def get_trend_at_date(self, date):
        return self.trend[date]
