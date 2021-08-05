# When crossover means change in trend, need other indicators as confirmation as there is a lot of false alarm
# Can check divergence with price as an indication of an impending trend reversal
# Extended period of momentum (+ve over -ve or vice versa) shows strength in trend
# Large and increasing difference between +ve and -ve also means price volatility
# Narrowing difference could mean consolidation
# https://www.investopedia.com/articles/technical/02/050602.asp
# https://www.investopedia.com/ask/answers/112814/what-directional-movement-index-dmi-formula-and-how-it-calculated.asp
import numpy as np
import pandas as pd
import talib

from main.util.enums import Trend


class DMI:
    def __init__(self, data: pd.DataFrame):
        self.trend = {}
        date = data.index
        dmi_plus = talib.PLUS_DI(data['HIGH'], data['LOW'], 14)
        dmi_minus = talib.MINUS_DI(data['HIGH'], data['LOW'], 14)
        dmi = talib.DX(data['HIGH'], 14)
        for index in date:
            if np.isnan(dmi_plus[index]) or np.isnan(dmi_minus[index]):
                self.trend[index] = Trend.UNKNOWN
            elif dmi_minus[index] < dmi_plus[index]:
                self.trend[index] = Trend.BUY
            elif dmi_minus[index] > dmi_plus[index]:
                self.trend[index] = Trend.SELL
            else:
                self.trend[index] = Trend.UNKNOWN

    def get_trend_at_date(self, date):
        return self.trend[date]
