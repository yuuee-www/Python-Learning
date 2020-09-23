import plotly.express as px

df = px.data.gapminder()

fig = px.scatter(df.query("year==2007"),x="gdpPercap", y="lifeExp", size="pop", color="continent", hover_name="country", log_x=True, size_max=60)

# Add a title and change the x-axis name
fig.update_layout(
    title='Life Expectancy v. Per Capita GDP, 2007',
    xaxis=dict(
        title='GDP per capita',
    ),
)

fig.show()
