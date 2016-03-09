# README.md
These are all pieces of code, scripts that allow you to monitor and track your cryptocurrency-related activity

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
This is a script designed for Google Sheets. By using various functions (and having your wallet address handy), you can monitor balances, conversions, and withdrawals from the comfort of your spreadsheet. As of right now this script supports Bitcoin and Dash. Here are a list of the functions.

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
=getTotalSent
```
Balance of a Dash address:
```
=getDashbalance
```
Bitcoin amount converted into U.S. dollars:
```
=getUSDconversion
```
