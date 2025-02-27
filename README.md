# brkb_garch_volatility_forecast

- This project forecasts the volatility of **$BRKB** (Berkshire Hathaway) stock returns using a GARCH(2,2) model from the ARCH library.
- It includes data preprocessing, rolling volatility predictions, and a 7-day future forecast visualized with Plotly.

---

## Files
- `brkb_vol_forecast.py`: Main script for fitting the GARCH model and forecasting volatility.
- `brkb.csv`: Dataset containing historical stock prices of $BRKB.
- `output.png`: Visualization of actual returns, rolling predicted volatility, and 7-day forecast.

---

## Libraries Used
- `pandas`
- `numpy`
- `arch`
- `plotly`

---

## Timeframe
- **Input**: Data ranges from **2023-11-03** to **2024-10-31** (from `brkb.csv`).
- **Output**: Rolling forecast for the last 365 days plus a 7-day future volatility forecast.
