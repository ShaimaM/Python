#Group Members:Shaima Alamri, Nada Alzahrani
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
# titanic data frame 
df = pd.read_csv('https://raw.githubusercontent.com/gumdropsteve/intro_to_python/main/day_09/data/titanic.csv')

df_1 = pd.DataFrame()
df_1['sex'] = ['Female','Female','Male','Male']
df_1['survivals'] = [1,0,0,1]
df_1['count'] = df.groupby(['Sex']).Survived.value_counts().to_list()

fig = px.bar(df_1, x="survivals", y = 'count', color = 'sex', barmode="group" )

fig2 = px.scatter(df, x='Pclass', y='Fare',
                 log_x=True, size_max=60)

fig3 = px.scatter(df, x='SibSp', y='Parch',
                 log_x=True, size_max=60)

app.layout = html.Div(children=[
    html.H1(children='Analyze Titanic Dataset '),

    html.Div(children='''
        Dash: A web application framework for Python.
    '''),

    html.Div(children= [
        html.H4(children = 'Total Number Of Survivals and Non Survivals Divided By Sex'),
        dcc.Graph(
        id='g1',
        figure=fig
        )]),
    
    html.Div(children= [
        html.H4(children = 'The Relation between the Passenger Class and the Fare Amount'),
        dcc.Graph(
        id='g2',
        figure=fig2) , 
        
        html.H4(children = 'The Relation between the Passenger With Siblings and spouses and Passengers with Parents and children '),
        dcc.Graph(
        id='g3',
        figure=fig3
        )]),

] , style={'text-align':'center'})

if __name__ == '__main__':
    app.run_server(debug=True)