import plotly
plotly.tools.set_credentials_file(username='wiesje95', api_key='VmOk5OJ6OVRbGjgCOjID')
import plotly.plotly as py
import plotly.graph_objs as go

def Plot3(list, string):
    plotly.offline.plot({
        "data": [go.Bar(x = ['C0.110','C1.112','A1.10','B0.201','A10.4','A1.06','A1.08'], y = list)],
        "layout": go.Layout(
            title = string,
            yaxis=dict(
                title='Percentage',
                titlefont=dict(
                    size=16,
                    color='rgb(107, 107, 107)'
                ),
                tickfont=dict(
                    size=14,
                    color='rgb(107, 107, 107)'
                )
            )
        )
    })
