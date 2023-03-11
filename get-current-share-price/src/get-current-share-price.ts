import axios from 'axios';

// Replace YOUR_API_KEY with your actual API key
const API_KEY = 'YOUR_API_KEY';
const TICKER = 'AAPL';

axios.get(`https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=${TICKER}&apikey=${API_KEY}`)
  .then(response => {
    const data = response.data['Global Quote'];
    const symbol = data['01. symbol'];
    const price = parseFloat(data['05. price']);
    console.log(`Current share value of ${symbol}: $${price}`);
  })
  .catch(error => {
    console.error(error);
  });
