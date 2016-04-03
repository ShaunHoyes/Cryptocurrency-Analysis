import time, json, requests

def BitcoinAverage():
    BitcoinAverageTick = requests.get('https://api.bitcoinaverage.com/ticker/USD/')
    return BitcoinAverageTick.json()['last']

print str(BitcoinAverage())
