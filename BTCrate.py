import urllib
 
def getBTC():
    try:
        url  = urllib.urlopen('http://api.bitcoincharts.com/v1/weighted_prices.json').read()
        usd  = url.split('"}, ')[0]
        rate = usd.split('"24h": "')[1]
        return rate
    except:
        return 'Unknown'
 
print(getBTC())
