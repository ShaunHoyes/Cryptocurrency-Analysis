from decimal import Decimal
from prettytable import PrettyTable
import time, json, requests

def btc():
    btcPrice = requests.get('https://www.cryptonator.com/api/ticker/btc-usd')
    return btcPrice.json()['ticker']['price']

def eth():
    ethPrice = requests.get('https://www.cryptonator.com/api/ticker/eth-usd')
    return ethPrice.json()['ticker']['price']

def ltc():
    ltcPrice = requests.get('https://www.cryptonator.com/api/ticker/ltc-usd')
    return ltcPrice.json()['ticker']['price']

def dash():
    dashPrice = requests.get('https://www.cryptonator.com/api/ticker/dash-usd')
    return dashPrice.json()['ticker']['price']

def sjcx():
    sjcxPrice = requests.get('https://www.cryptonator.com/api/ticker/sjcx-usd')
    return sjcxPrice.json()['ticker']['price']

def xcp():
    xcpPrice = requests.get('https://www.cryptonator.com/api/ticker/xcp-usd')
    return xcpPrice.json()['ticker']['price']

coins = PrettyTable(['Coin', 'Price'])



coins.add_row(['Bitcoin BTC:', "$" + btc() + "\n"])
coins.add_row(['Ethereum ETH:', "$" + eth() + "\n"])
coins.add_row(['Litecoin LTC:', "$" + ltc() + "\n"])
coins.add_row(['Dash DASH:', "$" + dash() + "\n"])
coins.add_row(['Counterparty XCP:', "$" + xcp() + "\n"])
coins.add_row(['Storjcoin SJCX:', "$" + sjcx()])

print coins;

