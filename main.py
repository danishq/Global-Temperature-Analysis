import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from dash import Dash, dcc, html
from dash.dependencies import Input, Output
import plotly.graph_objects as go

# Step 1: Load Data from JSON
file_path = "./months.json"
data = pd.read_json(file_path)

# Convert 'Year' to datetime and extract the year only
data['Year'] = pd.to_datetime(data['Year']).dt.year

# Aggregate data by year (average of monthly anomalies per year)
yearly_data = data.groupby('Year', as_index=False)['Mean'].mean()

# Convert to numpy arrays
years = np.array(yearly_data['Year'])
anomalies = np.array(yearly_data['Mean'])

# Step 2: Apply Moving Average for Smoothing
window_size = 5  # Adjust window for better smoothing
smoothed_anomalies = np.convolve(anomalies, np.ones(window_size)/window_size, mode='valid')

# Step 3: Matplotlib Visualization
plt.figure(figsize=(10, 6))
plt.plot(years[window_size-1:], smoothed_anomalies, label='Smoothed Anomaly', marker='o')
plt.xlabel('Year')
plt.ylabel('Temperature Anomaly (°C)')
plt.title('Global Temperature Anomalies (Yearly) with Smoothing')
plt.legend()
plt.grid(True)
plt.show()

# Step 4: Dash Interactive Visualization
app = Dash(__name__)

app.layout = html.Div([
    dcc.Graph(id='temperature-graph'),
    dcc.Slider(
        id='year-slider',
        min=int(years[window_size-1]),
        max=int(years[-1]),
        value=int(years[window_size-1]),
        marks={str(year): str(year) for year in years if year % 10 == 0},
        step=None
    )
])

@app.callback(
    Output('temperature-graph', 'figure'),
    [Input('year-slider', 'value')]
)
def update_graph(selected_year):
    filtered_data = yearly_data[yearly_data['Year'] <= selected_year]
    anomalies = np.array(filtered_data['Mean'])
    smoothed_anomalies = np.convolve(anomalies, np.ones(window_size)/window_size, mode='valid')
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=filtered_data['Year'][window_size-1:], y=smoothed_anomalies,
                             mode='lines+markers', name='Smoothed Anomaly'))
    fig.update_layout(title='Global Temperature Anomalies Over Time',
                      xaxis_title='Year', yaxis_title='Temperature Anomaly (°C)')
    
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)
