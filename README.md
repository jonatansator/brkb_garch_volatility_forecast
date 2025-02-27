# brkb_volatility_forecast

- This project forecasts the volatility of **$BRKB** (Berkshire Hathaway) stock returns using a GARCH(2,2) model from the `arch` library.
- It includes data preprocessing, rolling volatility predictions, a 7-day future forecast, and an interactive visualization.

---

## Files
- `brkb_volatility.py`: Main script for fitting the GARCH model and forecasting volatility.
- `brkb.csv`: Dataset containing historical stock prices of $BRKB with a `date` column and `close` prices.
- `output.png`: Plot

---

## Libraries Used
- `pandas`
- `numpy`
- `arch` 
- `plotly` 

---

## Timeframe
- **Input**: Historical data from `brkb.csv`
- **Rolling Forecast**: Volatility predictions for the last 365 days of the dataset.
- **Future Forecast**: Predicts volatility for the next 7 days beyond the last date in the data.
