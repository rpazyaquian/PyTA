__author__ = 'rebecca'

import pandas
import numpy as np


def sma(prices, n_periods):
    """
    Returns the rolling mean of a given list of stock prices "prices"
    over a period of time "n_periods". Interfaces with Pandas, so the details are
    sort of unknown to me.

    n_periods, for a typical SMA, is equivalent to the "days" it spans.
    So for a 50-day SMA, n_periods is equal to 50.

    Accepts: Array; integer.
    Return type: Array.
    """
    sma = pandas.rolling_mean(prices, n_periods, min_periods=n_periods)
    return sma  # Returns a Numpy array in this case


def bollinger_upper(prices, sma, n_periods):
    """
    Returns the upper Bollinger band line, for implementing a Bollinger
    band into the plot. Uses the list of stock prices "prices",
    the rolling mean returned by sma() "sma", over a number of periods "n_periods".
    You must use the same number of periods as used in the associated sma() function.
    Accepts: Array; array; integer.
    Return type: Array.
    """
    stdev = pandas.rolling_std(prices, n_periods, min_periods=n_periods)
    return sma + (2 * stdev)  # Returns a Numpy Array in this case


def bollinger_lower(prices, sma, n_periods):
    """
    Returns the lower Bollinger band line, for implementing a Bollinger
    band into the plot. Uses the list of stock prices "prices",
    the rolling mean returned by sma() "sma", over a number of periods "n_periods".
    You must use the same number of periods as used in the associated sma() function.
    Accepts: Array; array; integer.
    Return type: Array.
    """
    stdev = pandas.rolling_std(prices, n_periods, min_periods=n_periods)
    return sma - (2 * stdev)  # Returns a Numpy Array in this case


def stackify(x, y):
    """
    Stacks two arrays of data together. Used with Bollinger bands, at least for Bokeh.

    For example, in Bollinger bands, x would be the upper band data (which gets reversed)
    and y would be the lower band data (which has the reversed upper data appended).
    This would supply the y coordinates.

    The function still needs a little more work, since it's not very generalized.
    (Especially since it assumes the input is an array.)
    Accepts: Array 1; Array 2.
    Return type: Array.
    """

    stack = np.append(y, x[::-1])
    return stack


def rsi(prices, timeframe=14):
    """
    Returns the Relative Strength Index for a list of stock prices "prices"
    over a period of time "timeframe".
    Code shamelessly stolen from Sentdex. Sorry!

    Accepts: Array; integer (optional).
    Return type: Array.
    """

    delta = np.diff(prices)
    seed = delta[:timeframe + 1]

    up = seed[seed >= 0].sum() / timeframe
    down = -seed[seed < 0].sum() / timeframe

    rs = up / down

    rsi = np.zeros_like(prices)
    rsi[:timeframe] = 100. - (100. / (1. + rs))

    for i in range(timeframe, len(prices)):

        i_delta = delta[i - 1]

        if i_delta > 0:
            upval = i_delta
            downval = 0.
        else:
            upval = 0.
            downval = -i_delta

        up = (up * (timeframe - 1) + upval) / timeframe
        down = (down * (timeframe - 1) + downval) / timeframe

        rs = up / down
        rsi[i] = 100. - (100. / (1. + rs))

    return rsi  # Returns a Numpy Array.


def ema(prices, n_periods):
    """
    Returns the exponentially weighted moving average of a given SMA "sma".

    A MACD requires a 12-day EMA, a 26-day EMA, and a 9-day EMA.
    When writing an EMA, we need to figure out how to say "give me an n-day EMA".
    n_periods is the number of days you want it to span.
    So, a 12-day EMA would have n_periods=12.

    Accepts: Array; float.
    Return type: Array.
    """

    span = n_periods

    ema = pandas.ewma(prices, span=span)
    return ema


def macd_line(prices):
    """
    Returns the Moving Average Convergence-Divergence (MACD) of a given set of price data.
    This is the main line for plotting on a chart.

    Accepts: Array.
    Return type: Array.
    """

    ema12 = pandas.ewma(prices, span=12)
    ema26 = pandas.ewma(prices, span=26)

    macd = ema12 - ema26
    return macd


def macd_signal(prices):
    """
    Returns the MACD signal line of a given set of price data.

    Accepts: Array.
    Return type: Array.
    """

    ema9 = pandas.ewma(prices, span=9)

    return ema9


def macd_hist(prices):
    """
    Returns the MACD histogram data for a given set of price data.

    Accepts: Array.
    Return type: Array.
    """

    ema9 = pandas.ewma(prices, span=9)
    ema12 = pandas.ewma(prices, span=12)
    ema26 = pandas.ewma(prices, span=26)

    hist = (ema12 - ema26) - ema9
    return hist