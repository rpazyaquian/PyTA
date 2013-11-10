PyTA
====

Python library for performing computed technical analysis on stock data statistics. Inspired by TA-Lib.

====

> What is this?

PyTA is a Python module inspired by TA-Lib.
TA-Lib is a C library for performing technical analysis on stock data, like the kind you would get from Yahoo! Finance.
It has a very comprehensive list of functions and algorithms for technical analysis indicators.

Indicators are calculations that aim to measure certain things about stock data such as "money flow, trends, volatility and momentum". (Thanks, Investopedia!)
You calculate indicators given a point in time and a set of data, and compare them to your raw stock data.
Technical analysis aims to use these indicators as a way of predicting the stock market.

> How are you going to do this?

I'm still not sure if I'm aiming to flat-out recreate TA-Lib, or if I'm going to start from scratch.
I think that the functions I'll implement are, at first, going to be relatively simple.
For example, getting the Simple Moving Average (50-day and 200-day).
From there, I'll work my way up to complicated stuff like "Kaufmann Adaptive Moving Average".

> WHY are you doing this?

TA-Lib is for C, not Python, and I'm used to working in Python.
The automatic TA program I wrote was in Python, after all.
Trying to port TA-Lib to Python through a wrapper was a bit difficult for me.
Plus, the documentation leaves something to be desired (IMO).

Basically, TA-Lib isn't native to Python and doesn't have adequate documentation for my purposes.
I want to use a technical analysis library, so I might as well write my own.

> Isn't this going to require a lot of statistics?

Well, yes. I'm going to have to understand how to calculate these indicators, what inputs I need, etc.
I...don't have a great foundation in statistics. But for now, simply figuring out how to properly write the algorithms should suffice.

> How big is this project going to be?

This is going to be purely defining the indicators and their algorithms.
I'm not going to add an API for Yahoo! Finance or anything (yet).

> What about oscillators?

Oscillators are a bit more complicated, but I'm going to include them at some point. I will! Really! Don't look at me like that.

> "Pee-ta"?

Pee-ta. It's a work in progress. I can change the name.
