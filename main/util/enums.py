from enum import Enum


class Trend(Enum):
    BUY = 1
    SELL = -1
    UNKNOWN = None
    BREAKOUT = 0
