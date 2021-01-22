#Group Members:Shaima Alamri, Nada Alzahrani and Abeer Alghamdi .
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

df_2 = pd.DataFrame()
df_2['Survivals'] = df.Survived.value_counts().index
df_2['count'] = df.Survived.value_counts()

df_3 = pd.DataFrame()
df_3['Pclass'] = ['1' , '1' , '2' , '2' , '3' , '3']
df_3['survivals'] = [1,0,0,1,0,1]
df_3['count'] = df.groupby(['Pclass']).Survived.value_counts().to_list()

df_4 = pd.DataFrame()
df_4['Pclass'] = df.groupby(['Pclass']).Fare.sum().index
df_4['sum'] = df.groupby(['Pclass']).Fare.sum().to_list()

fig1 = px.bar(df_2, x="Survivals", y = 'count', barmode="group" )

fig = px.bar(df_1, x="survivals", y = 'count', color = 'sex', barmode="group" )

fig2 = px.bar(df_4, x='Pclass', y='sum' , barmode="group")

fig3 = px.scatter(df, x='SibSp', y='Parch',
                 log_x=True, size_max=60)

fig4 = px.bar(df_3, x="survivals", y = 'count', color = 'Pclass', barmode="group" )

fig5 = px.scatter(df, x='Age' , y="SibSp" ,log_x=True, size_max=60)

fig6 = px.scatter(df, x='Age' , y="Parch" ,log_x=True, size_max=60)

fig7 = px.histogram(df, x="Age")

fig8 = px.scatter(df, x='Age', y='Fare',log_x=True, size_max=60)

no_children = df.loc[df.Age < 16].Age.count()
no_adults = df.shape[0] - no_children
df_5 = pd.DataFrame()
df_5['Age'] = ['Children' , 'Adults']
df_5['count'] = [no_children , no_adults]
fig9 = px.pie(df_5, values='count' , names='Age')

fig10 = px.pie(df_2, values='count' , names='Survivals')

fig11 = px.scatter(df, x='Age', y='Fare', color = 'Survived' , log_x=True, size_max=60)

app.layout = html.Div(children=[
    html.H1(children='Addressing Passengers Of Titanic'),

    html.Div(children='''
        Dash Made by : Nada ALzahrani, Shaima Alamri, Abeer Alghamdi
    '''),

    html.H4(children = 'Total Number Of Survivals and Non Survivals'),
    html.Div(children= [
        dcc.Graph(
        id='g4',
        figure=fig1,)
    ] , style =  {'display': 'inline-block'}),
    
    html.Div(children= [
        dcc.Graph(
        id='g11',
        figure=fig10
        )], style =  {'display': 'inline-block'}),
    
    html.Div(children= [
        html.H4(children = 'Total Number Of Survivals and Non Survivals Divided By Sex'),
        dcc.Graph(
        id='g1',
        figure=fig
        )]),
    
    html.Div(children= [
        html.H4(children = 'Total Number Of Survivals and Non Survivals Divided By Passenger Class'),
        dcc.Graph(
        id='g5',
        figure=fig4
        )]),
    
    html.Div(children= [
        html.H4(children = 'The Relation between Passenger Age and Number Of Siblings and spouses'),
        dcc.Graph(
        id='g6',
        figure=fig5
        )]),
    
    html.Div(children= [
        html.H4(children = 'Age Distribution Using Histogram'),
        dcc.Graph(
        id='g8',
        figure=fig7
        )]),
    
    html.Div(children= [
        html.H4(children = 'The Relation between Passenger Age and Number Of Parents and children'),
        dcc.Graph(
        id='g7',
        figure=fig6
        )]),
    
    html.Div(children= [
        html.H4(children = 'The Relation between the Passenger With Siblings and spouses and Passengers with Parents and children '),
        dcc.Graph(
        id='g3',
        figure=fig3
        )]),
    
    html.Div(children= [
        html.H4(children = 'The Total Fare Amount For Each Passeger Class'),
        dcc.Graph(
        id='g2',
        figure=fig2
        )]), 
    
    html.Div(children= [
        html.H4(children = 'The Relation between the Passenger Age and the Fare Amount'),
        dcc.Graph(
        id='g9',
        figure=fig8
        )]), 
    
    html.Div(children= [
        html.H4(children = 'The Relation between the Passenger Age and the Fare Amount With The Colour indicating Survivals'),
        dcc.Graph(
        id='g12',
        figure=fig11
        )]), 

    
        html.Div(children= [
        html.H4(children = 'The Number Of Adults And Children'),
        dcc.Graph(
        id='g10',
        figure=fig9
        )]), 
    
] , style={'text-align':'center'})

if __name__ == '__main__':
    app.run_server(debug=True)
