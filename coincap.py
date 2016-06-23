from decimal import Decimal
from prettytable import PrettyTable

import time, json, requests
import sys

BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE = range(8)

def has_colours(stream):
    if not hasattr(stream, "isatty"):
        return False
    if not stream.isatty():
        return False # auto color only on TTYs
    try:
        import curses
        curses.setupterm()
        return curses.tigetnum("colors") > 2
    except:
        # guess false in case of error
        return False
has_colours = has_colours(sys.stdout)


def printout(text, colour=WHITE):
        if has_colours:
                seq = "\x1b[0;%dm" % (30+colour) + text + "\x1b[0m"
                sys.stdout.write(seq)
        else:
                sys.stdout.write(text)

def price():
    totalPrice = requests.get('http://www.coincap.io/global')
    return round(float(totalPrice.json()['btcPrice']), 2)

def cap():
    btcCap = requests.get('http://www.coincap.io/global')
    return round(float(btcCap.json()['btcCap']), 2)

def alt():
    altCap = requests.get('http://www.coincap.io/global')
    return round(float(altCap.json()['altCap']), 2)

def dom():
    domIndex = requests.get('http://www.coincap.io/global')
    return round(float(domIndex.json()['dom']), 2)

def bitNodes():
    node = requests.get('http://www.coincap.io/global')
    return round(float(node.json()['bitnodesCount']), 0)


table = PrettyTable(["Item", "Calculation"])

"""
print("BTC Marketcap: " + str(cap())
print("Altcoin Marketcap: " + "$" + str(alt() + "\n")
print("Domination Index: " + str(dom() + " %" + "\n")
print("Bitnodes Count: " + str(bitNodes()
"""


table.add_row(['BTC/USD: ', "$" + str(price()) + "\n"])
table.add_row(['BTC Marketcap: ', "$" + str(cap()) + "\n"])
table.add_row(['Altcoin Marketcap: ', "$" + str(alt()) + "\n"])
table.add_row(['Domination Index: ', str(dom()) + " %" + "\n"])
table.add_row(['Bitnodes Count: ', str(bitNodes())])


print("\n")
printout("Coincap.io Market Metrics" + "\n", GREEN)
print(table)
print("\n")
