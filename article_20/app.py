import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas
import plotly.express as px

app = dash.Dash(__name__)

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

data_frame = pandas.DataFrame({
    "Day": ["Mon", "Tue", "Wed", "Thur", "Fri", "Sat", "Sun", "Mon", "Tue", "Wed", "Thur", "Fri", "Sat", "Sun"],
    "Value": [9.5, 8.7, 8.8, 8.5, 10.0, 10.3, 9.6, 40.0, 40.0, 39.0, 39.0, 42.0, 41.0, 37.0],
    #"Value": [9, 8, 8, 8, 10, 10, 9, 40, 40, 39, 39, 42, 41, 37],
    "Measure": ["HR", "HR", "HR", "HR", "HR", "HR", "HR", "HRV", "HRV", "HRV", "HRV", "HRV", "HRV", "HRV"]
})

fig = px.bar(data_frame, x="Day", y="Value", color="Measure", barmode="group")

fig.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)

app.layout = html.Div(style={'backgroundColor': colors['background']},children=[
    html.H1(children='Hello My First Dash',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),
    
    html.Div(children='''
        Dash: Tracking My HR/HRV Data.''',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),

    dash.dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
  app.run_server(debug=True)
