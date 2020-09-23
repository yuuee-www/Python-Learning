import plotly.express as px

df = px.data.gapminder()

fig = px.scatter(df, 
                 x="gdpPercap", 
                 y="lifeExp", 
                 animation_frame="year", 
                 animation_group="country", 
                 size="pop", 
                 color="continent", 
                 hover_name="country", 
                 log_x = True, 
                 size_max=60,
                 )

fig.update_layout(
    title='Life Expectancy v. Per Capita GDP, 1952 - 2007',
    xaxis=dict(
        title='GDP per capita',
    ),
    yaxis=dict(
        title='Life Expectancy (years)',
    ),
)

fig.show()
