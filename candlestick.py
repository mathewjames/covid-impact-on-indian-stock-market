# %%
import plotly.graph_objects as go
import plotly
import pandas as pd

# %%
adani_df = pd.read_csv('Data\Line Graph\ADANIENT_day_data_processed.csv')
adani_df['company'] = 'ADANI'
appolo_df = pd.read_csv('Data\Line Graph\APOLLOHOSP_day_data_processed.csv')
appolo_df['company'] = 'APPOLO'
asian_df = pd.read_csv('Data\Line Graph\ASIANPAINT_day_data_processed.csv')
asian_df['company'] = 'ASIAN PAINTS'
airtel_df = pd.read_csv('Data\Line Graph\BHARTIARTL_day_data_processed.csv')
airtel_df['company'] = 'AIRTEL'
drreddy_df = pd.read_csv('Data\Line Graph\DRREDDY_day_data_processed.csv')
drreddy_df['company'] = 'DR. REDDY'
infy_df = pd.read_csv('Data\Line Graph\INFY_day_data_processed.csv')
infy_df['company'] = 'INFOSYS'
itc_df = pd.read_csv('Data\Line Graph\ITC_day_data_processed.csv')
itc_df['company'] = 'ITC'
lt_df = pd.read_csv('Data\Line Graph\LT_day_data_processed.csv')
lt_df['company'] = 'L&T'
nifty_df = pd.read_csv(r'Data\Line Graph\NIFTY 50_day_data_processed.csv')
nifty_df['company'] = 'NIFTY 50'
rel_df = pd.read_csv('Data\Line Graph\RELIANCE_day_data_processed.csv')
rel_df['company'] = 'RELIANCE'
tatam_df = pd.read_csv('Data\Line Graph\TATAMOTORS_day_data_processed.csv')
tatam_df['company'] = 'TATA MOTORS'

# %%
df_stocks = pd.concat([nifty_df, adani_df, appolo_df, asian_df, airtel_df, drreddy_df, infy_df, itc_df, lt_df, rel_df, tatam_df], axis=0)
df_stocks

# %%
fig = go.Figure()
j=0
for company in df_stocks['company'].unique():
    fig.add_trace(
        go.Candlestick(
            x = df_stocks['date'][df_stocks['company'] == company],
            open=df_stocks['open'][df_stocks['company'] == company],
            high=df_stocks['high'][df_stocks['company'] == company],
            low=df_stocks['low'][df_stocks['company'] == company],
            close=df_stocks['close'][df_stocks['company'] == company],
            name = company, visible = False,
        )
    )
    fig.update_layout(
    shapes = [dict(
        x0='2020-03-21', x1='2020-03-21', y0=0, y1=1, xref='x', yref='paper',
        line_width=2)],
    annotations=[dict(
        x='2020-03-21', y=1, xref='x', yref='paper',
        showarrow=False, xanchor='left', text='Increase After the Covid Fall')]
    )
    j+=1

fig.data[0].visible = True

buttons = []
i = 0
for company in df_stocks['company'].unique():
    args = [False] * len(df_stocks['company'].unique())
    args[i] = True

    button = dict(label = company,
                  method = "update",
                  args=[{"visible": args}])
    
    #add the button to our list of buttons
    buttons.append(button)
    
    #i is an iterable used to tell our "args" list which value to set to True
    i+=1

fig.update_layout(
    title='Covid Stock Data',
    title_x=0.5,
    yaxis_title='Price',
    updatemenus=[
    dict(active=0,
        type="dropdown",
        x = .0009,
        y = 1.04,
        buttons=buttons,
        xanchor="left",
        yanchor="bottom",
    )
])

plotly.offline.plot(fig, filename='candlestick.html')

# %%
