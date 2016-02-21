#!/bin/bash
# Credit to David Walsh - <https://davidwalsh.name/bitcoin>

echo "Coindesk BTC price USD: "

while [ 1 ] # while always
do
curl -s http://api.coindesk.com/v1/bpi/currentprice.json |
python -c "import json, sys; print json.load(sys.stdin)['bpi']['USD']['rate']"
printf "\033[A" # restarts the script
sleep 10 # price will refresh every 10 seconds
done
