/* Returns the most recent balance of a bitcoin address */ 

function getBalance(btcAddress) {
  var response = UrlFetchApp.fetch('http://blockchain.info/address/' + btcAddress + '?format=json');
  var json = response.getContentText();
  var data = JSON.parse(json);
  return data.final_balance * Math.pow(10,-8); 
  /* The figure returned is the balance in satoshis. 
  The Math.pow funcitons allows us 
  to read this balance in whole bitcoin numbers. */
}

/* Returns all bitcoin ever received by a bitcoin address */

function getReceived(btcAddress) {
  var response = UrlFetchApp.fetch('http://blockchain.info/address/' + btcAddress + '?format=json');
  var json = response.getContentText();
  var data = JSON.parse(json);
  return data.total_received * Math.pow(10,-8);
}

/* Returns all bitcoin ever sent by a bitcoin address */

function getTotalSent(btcAddress) {
  var response = UrlFetchApp.fetch('http://blockchain.info/address/' + btcAddress + '?format=json');
  var json = response.getContentText();
  var data = JSON.parse(json);
  return (data.total_received * Math.pow(10,-8)) - (data.final_balance * Math.pow(10,-8));
}

/* Returns the balance of a Dash address */

function getDashBalance(dashAddress) {
  var response = UrlFetchApp.fetch('http://explorer.darkcoin.io/chain/Dash/q/addressbalance/' + dashAddress);
  var json = response.getContentText();
  var data = JSON.parse(json);
  return data;
}

/* Returns a bitcoin amount converted into U.S. dollars */

function USDconversion(bitcoinAmount) {
  var response = UrlFetchApp.fetch('https://api.bitcoinaverage.com/ticker/global/USD/last');
  return response * bitcoinAmount;
}

