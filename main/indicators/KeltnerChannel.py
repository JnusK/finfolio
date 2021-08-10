# Keltner Channel is a volatility based envelop, with the lower line as support and upper line as resistance.
# The lower line is EMA - 2 * ATR and the upper line is EMA + 2 * ATR. The middle line is EMA.
# Typical EMA period is 20 days.
# A bullish breakout happens when price breaches the upper line, especially if envelop is trending upwards after a sideways period. A bearish breakout is when price breaches the lower line, especially if envelop is trending upwards after a sideways period.
# If the price is constantly hitting the lower band, but not the upper, when the price does finally reach the upper band it could be a signal that the downtrend is near an end and vice versa.
# https://www.investopedia.com/terms/k/keltnerchannel.asp

import pandas as pd
import talib

from main.util.enums import Trend


class KeltnerChannel:
    def __init__(self, data: pd.DataFrame):
        self.trend = {}
        ema = talib.EMA(data['close'], 20)
        atr = talib.ATR(data['high'], data['low'], data['close'], 20)
        keltner_upper = ema + 2 * atr
        keltner_lower = ema - 2 * atr
