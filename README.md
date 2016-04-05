# README.md
These are all scripts that allow you to monitor and track your cryptocurrency-related activity. 

# Coindesk Price Ticker
This is a script that allows you to retrieve the real-time price of bitcoin in your terminal

After saving the script file (btc.sh), you will want to make sure that the file is executable:

```
$ chmod +x the_file_name
```

Now everything should be set. If you ever want to check the price of Bitcoin from the terminal, just type the following:
```
$ ./btc.sh
```

# Crytpocurrency Sheet Analysis
These scripts are designed to work within Google Sheets. By using various functions (and having your wallet address handy), you can monitor balances, conversions, and withdrawals all from the spreadsheet. As of right now these scripts retrieve Bitcoin, Ether, and Dash balances.

Current balance of a bitcoin address:
```
=getBalance()
```
Total amount ever recieved by a bitcon address:
```
=getReceived()
```
Total amount ever sent from a bitcoin address:
```
=getTotalSent()
```
Balance of a Dash address:
```
=getDashBalance()
```
Bitcoin amount converted into U.S. dollars:
```
=getUSDconversion()
```
Current balance of a given ether address:
```
=getEthBalance()
```

# Coin Table
With Coin Table, you should get an output that looks like this:
```
+-------------------+---------------+
|        Coin       |     Price     |
+-------------------+---------------+
|    Bitcoin BTC:   | $421.66598490 |
|                   |               |
|   Ethereum ETH:   |  $10.78536699 |
|                   |               |
|   Litecoin LTC:   |  $3.25221028  |
|                   |               |
|     Dash DASH:    |  $7.19095736  |
|                   |               |
|    Factom FCT:    |  $1.63825247  |
|                   |               |
| Counterparty XCP: |  $2.19433714  |
|                   |               |
|  Storjcoin SJCX:  |  $0.08874382  |
+-------------------+---------------+
```
