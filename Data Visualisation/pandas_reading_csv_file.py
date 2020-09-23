import pandas as pd
import plotly.express as px

# Example reading data from a CSV file that is saved online at a URL (see https://plotly.com/python/plot-data-from-csv/)
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/2014_apple_stock.csv')

fig = px.line(df, x = 'AAPL_x', y = 'AAPL_y', title='Apple Share Prices over time (2014)',)

fig.update_layout(
    xaxis=dict(
        title='Date',
    ),
    yaxis=dict(
        title='Share price',
    ),
)

fig.show()
