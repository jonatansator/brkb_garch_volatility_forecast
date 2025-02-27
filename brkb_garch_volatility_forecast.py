import pandas as pd
import numpy as np
from arch import arch_model
import plotly.graph_objects as go
from datetime import datetime, timedelta

# Step 1: Load and prepare the data
df = pd.read_csv('brkb.csv', parse_dates=['date'], index_col='date')
X = 100 * df['close'].pct_change().dropna()

# Step 2: Define the GARCH model
mdl = arch_model(X, p=2, q=2)
fit = mdl.fit(disp='off')

# Step 3: Perform rolling forecast
test_len = 365
preds = []
for i in range(test_len):
    train = X[:-(test_len-i)]
    m = arch_model(train, p=2, q=2)
    res = m.fit(disp='off')
    fc = res.forecast(horizon=1)
    preds.append(np.sqrt(fc.variance.values[-1, 0]))
preds = pd.Series(preds, index=X.index[-test_len:])

# Step 4: Forecast future volatility
last_fit = mdl.fit(disp='off')
future = last_fit.forecast(horizon=7)
dates = [X.index[-1] + timedelta(days=i) for i in range(1, 8)]
Y = pd.Series(np.sqrt(future.variance.values[-1, :]), index=dates)

# Step 5: Create Plotly visualization
fig = go.Figure()

# Add actual returns
fig.add_trace(go.Scatter(
    x=X.index[-test_len:], y=X[-test_len:],
    mode='lines', name='Actual Returns',
    line=dict(color='#FF6B6B', width=1)
))

# Add predicted volatility (rolling)
fig.add_trace(go.Scatter(
    x=preds.index, y=preds,
    mode='lines', name='Predicted Volatility',
    line=dict(color='#4ECDC4', width=1, dash='dash')
))

# Add future forecast
fig.add_trace(go.Scatter(
    x=Y.index, y=Y,
    mode='lines', name='7-Day Forecast',
    line=dict(color='#4ECDC4', width=1, dash='dash')
))

# Customize layout
fig.update_layout(
    title='BRK.B Volatility Forecast',
    title_font_color='white',
    plot_bgcolor='rgb(40, 40, 40)',
    paper_bgcolor='rgb(40, 40, 40)',
    font=dict(color='white'),
    xaxis=dict(gridcolor='rgba(255, 255, 255, 0.1)', gridwidth=0.5),
    yaxis=dict(gridcolor='rgba(255, 255, 255, 0.1)', gridwidth=0.5),
    margin=dict(l=50, r=50, t=50, b=50),
    legend=dict(font=dict(color='white'))
)

fig.show()