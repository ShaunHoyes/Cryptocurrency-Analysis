#!/usr/bin/env python3

from decimal import Decimal
from prettytable import PrettyTable

import time, json, requests

def btc():
    btcPrice = requests.get('https://www.cryptonator.com/api/ticker/btc-usd')
    return round(float(btcPrice.json()['ticker']['price']), 2)

def eth():
    ethPrice = requests.get('https://www.cryptonator.com/api/ticker/eth-usd')
    return round(float(ethPrice.json()['ticker']['price']), 2)

def ltc():
    ltcPrice = requests.get('https://www.cryptonator.com/api/ticker/ltc-usd')
    return round(float(ltcPrice.json()['ticker']['price']), 2)

def dash():
    dashPrice = requests.get('https://www.cryptonator.com/api/ticker/dash-usd')
    return round(float(dashPrice.json()['ticker']['price']), 2)

def sjcx():
    sjcxPrice = requests.get('https://www.cryptonator.com/api/ticker/sjcx-usd')
    return round(float(sjcxPrice.json()['ticker']['price']), 2)

def xcp():
    xcpPrice = requests.get('https://www.cryptonator.com/api/ticker/xcp-usd')
    return round(float(xcpPrice.json()['ticker']['price']), 2)


coins = PrettyTable(['Coin', 'Price'])

coins.add_row(['Bitcoin BTC:', "$" + str(btc()) + "\n"])
coins.add_row(['Ethereum ETH:', "$" + str(eth()) + "\n"])
coins.add_row(['Litecoin LTC:', "$" + str(ltc()) + "\n"])
coins.add_row(['Dash DASH:', "$" + str(dash()) + "\n"])
coins.add_row(['Counterparty XCP:', "$" + str(xcp()) + "\n"])
coins.add_row(['Storjcoin SJCX:', "$" + str(sjcx()) + "\n"])


print(coins);
