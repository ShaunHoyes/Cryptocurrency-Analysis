from prettytable import PrettyTable

import json, requests

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

table.add_row(['BTC/USD: ', "$" + str(price()) + "\n"])
table.add_row(['BTC Marketcap: ', "$" + str(cap()) + "\n"])
table.add_row(['Altcoin Marketcap: ', "$" + str(alt()) + "\n"])
table.add_row(['Domination Index: ', str(dom()) + " %" + "\n"])
table.add_row(['Bitnodes Count: ', str(bitNodes())])

print("\n")
print("Coincap.io Market Metrics")
print(table)
print("\n")
