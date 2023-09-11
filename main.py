import pandas as pd
import plotly.graph_objects as go
from sklearn.cluster import KMeans
import numpy as np

# Read the CSV file into a DataFrame
df = pd.read_csv('data_panel_1_day.csv')
df['timestamp'] = pd.to_datetime(df['timestamp'])
df.set_index('timestamp', inplace=True)

def kmeans_support_resistance(data, max_clusters=10):
    prices = data['close'].values.reshape(-1, 1)
    
    # Elbow method
    sum_of_squared_distances = []
    K = range(1, max_clusters+1)
    for k in K:
        km = KMeans(n_clusters=k)
        km = km.fit(prices)
        sum_of_squared_distances.append(km.inertia_)

    deltas = np.diff(sum_of_squared_distances)
    optimal_clusters = np.argwhere(deltas > np.mean(deltas)).flatten()[0] + 1
    
    kmeans = KMeans(n_clusters=optimal_clusters)
    kmeans.fit(prices)
    cluster_centers = kmeans.cluster_centers_
    support_resistance_levels = np.sort(cluster_centers, axis=0)
    
    return support_resistance_levels

# Manually set your zoom window (start and end dates)
start_date = 'YYYY-MM-DD'  # Replace with your start date
end_date = 'YYYY-MM-DD'    # Replace with your end date
zoomed_df = df[start_date:end_date]

# Get support and resistance levels for the zoomed window
levels = kmeans_support_resistance(zoomed_df)

# Current price (latest close price in the zoomed window)
current_price = zoomed_df['close'].iloc[-1]

# Create a candlestick chart for the zoomed window with Plotly
fig = go.Figure(data=[go.Candlestick(x=zoomed_df.index,
                open=zoomed_df['open'],
                high=zoomed_df['high'],
                low=zoomed_df['low'],
                close=zoomed_df['close'])])

# Add horizontal lines for support and resistance
for level in levels:
    if level[0] < current_price:
        color = 'green'  # Support
    else:
        color = 'red'    # Resistance

    fig.add_trace(go.Scatter(x=zoomed_df.index, y=[level[0]]*len(zoomed_df.index), mode='lines', line=dict(color=color), showlegend=False))

fig.update_layout(title='Zoomed Stock Data with Support and Resistance')
fig.update_layout(dragmode='zoom', xaxis=dict(fixedrange=False, range=[start_date, end_date]), yaxis=dict(fixedrange=False))
fig.show()
