import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import pandas_datareader.data as web
from dash.dependencies import Input, Output, State
from datetime import datetime

app=dash.Dash()


format=pd.read_csv('../Plotly-Dashboards-with-Dash-master/Data/NASDAQcompanylist.csv')
format.set_index('Symbol',inplace=True)

options=[]
for tic in format.index:
    dict={}
    dict['label']=format.loc[tic]['Name']+ ' ' + tic
    dict['value']=tic
    options.append(dict)



app.layout= html.Div([

            html.H1('Stock Dashboard'),

            html.Div([
                        html.H3('Enter Stock Symbol: ',style={'paddingRight':'30px'}),
                        dcc.Dropdown(id='stock_input',
                                   value=['TSLA'],
                                   options=options,
                                   multi=True
                                    )],style={'display':'inline-block','verticalAlign':'top','width':'30%'}),

            html.Div([

                            html.H3('Select Start and End Date: '),
                            dcc.DatePickerRange(id='datetimerange',
                                                min_date_allowed=datetime(2010,1,1),
                                                max_date_allowed=datetime.today(),
                                                start_date=datetime(2020,1,1),
                                                end_date=datetime.today()
                                                )

            ],style={'display':'inline-block'}),

            html.Div([
                    html.Button(id='button',
                                n_clicks=0,
                                children='Submit',
                                style={'fontSize':24,'marginLeft':'30px'})
            ],style={'display':'inline-block'}),

            dcc.Graph(id='graph',
                      figure={
                                'data':{'x':[1,4],'y':[1,4]},
                                'layout':{'title':'Default time'}

                          })

])

@app.callback(Output('graph','figure'),
              [Input('button','n_clicks')],
              [State('stock_input','value'),
               State('datetimerange','start_date'),
               State('datetimerange','end_date')])
def updata(n_clicks,stock_input,start_date,end_date):
    start=datetime.strptime(start_date[:10],'%Y-%m-%d')
    end=datetime.strptime(end_date[:10],'%Y-%m-%d')

    traces=[];
    for input in stock_input:
            data=web.DataReader(input,'yahoo',start,end)
            traces.append({'x':data.index,
                           'y':data['Close'],
                           'name':input})

    fig={
            'data':traces,
            'layout':{'title':stock_input}
    }

    return fig


if __name__ == '__main__':
    app.run_server()
