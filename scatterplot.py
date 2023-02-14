# %%
import pandas as pd
import plotly.io as pio
import plotly.express as px
import plotly

# %%
adani_df = pd.read_csv('Data\Scatterplot\ADANIENT_day_data_processed.csv', parse_dates=['date'], index_col=['date'])
appolo_df = pd.read_csv('Data\Scatterplot\APOLLOHOSP_day_data_processed.csv', parse_dates=['date'], index_col=['date'])
asian_df = pd.read_csv('Data\Scatterplot\ASIANPAINT_day_data_processed.csv', parse_dates=['date'], index_col=['date'])
airtel_df = pd.read_csv('Data\Scatterplot\BHARTIARTL_day_data_processed.csv', parse_dates=['date'], index_col=['date'])
bajaj_df = pd.read_csv('Data\Scatterplot\BAJFINANCE_day_data_processed.csv', parse_dates=['date'], index_col=['date'])
divis_df = pd.read_csv('Data\Scatterplot\DIVISLAB_day_data_processed.csv', parse_dates=['date'], index_col=['date'])
drreddy_df = pd.read_csv('Data\Scatterplot\DRREDDY_day_data_processed.csv', parse_dates=['date'], index_col=['date'])
hind_df = pd.read_csv('Data\Scatterplot\HINDALCO_day_data_processed.csv', parse_dates=['date'], index_col=['date'])
hdfc_df = pd.read_csv('Data\Scatterplot\HDFC_day_data_processed.csv', parse_dates=['date'], index_col=['date'])
hul_df = pd.read_csv('Data\Scatterplot\HINDUNILVR_day_data_processed.csv', parse_dates=['date'], index_col=['date'])
infy_df = pd.read_csv('Data\Scatterplot\INFY_day_data_processed.csv', parse_dates=['date'], index_col=['date'])
itc_df = pd.read_csv('Data\Scatterplot\ITC_day_data_processed.csv', parse_dates=['date'], index_col=['date'])
lt_df = pd.read_csv('Data\Scatterplot\LT_day_data_processed.csv', parse_dates=['date'], index_col=['date'])
mm_df = pd.read_csv('Data\Scatterplot\MM_day_data_processed.csv', parse_dates=['date'], index_col=['date'])
nestle_df = pd.read_csv(r'Data\Scatterplot\NESTLEIND_day_data_processed.csv', parse_dates=['date'], index_col=['date'])
ongc_df = pd.read_csv('Data\Scatterplot\ONGC_day_data_processed.csv', parse_dates=['date'], index_col=['date'])
power_df = pd.read_csv('Data\Scatterplot\POWERGRID_day_data_processed.csv', parse_dates=['date'], index_col=['date'])
rel_df = pd.read_csv('Data\Scatterplot\RELIANCE_day_data_processed.csv', parse_dates=['date'], index_col=['date'])
sbi_df = pd.read_csv('Data\Scatterplot\SBIN_day_data_processed.csv', parse_dates=['date'], index_col=['date'])
sun_df = pd.read_csv('Data\Scatterplot\SUNPHARMA_day_data_processed.csv', parse_dates=['date'], index_col=['date'])
tatam_df = pd.read_csv('Data\Scatterplot\TATAMOTORS_day_data_processed.csv', parse_dates=['date'], index_col=['date'])
tcs_df = pd.read_csv('Data\Scatterplot\TCS_day_data_processed.csv', parse_dates=['date'], index_col=['date'])
ulttech_df = pd.read_csv(r'Data\Scatterplot\ULTRACEMCO_day_data_processed.csv', parse_dates=['date'], index_col=['date'])
upl_df = pd.read_csv(r'Data\Scatterplot\UPL_day_data_processed.csv', parse_dates=['date'], index_col=['date'])
wipro_df = pd.read_csv(r'Data\Scatterplot\WIPRO_day_data_processed.csv', parse_dates=['date'], index_col=['date'])

# %%
adani_df['company'] = 'Adani Enterprises'
appolo_df['company'] = 'Apollo Hospitals'
asian_df['company'] = 'Asian Paints'
airtel_df['company'] = 'Bharti Airtel'
bajaj_df['company'] = 'Bajaj Finance'
drreddy_df['company'] = "Dr. Reddy's Laboratories"
hdfc_df['company'] = "HDFC Bank"
infy_df['company'] = 'Infosys'
itc_df['company'] = 'ITC'
lt_df['company'] = 'Larsen & Toubro'
mm_df['company'] = 'Mahindra & Mahindra'
nestle_df['company'] = 'Nestle India'
ongc_df['company'] = 'Oil and Natural Gas Corporation'
rel_df['company'] = 'Reliance Industries'
sbi_df['company'] = 'State Bank of India'
divis_df['company'] = "Divi's Laboratories"
hind_df['company'] = 'Hindalco Industries'
hul_df['company'] = 'Hindustan Unilever'
power_df['company'] = 'Power Grid Corporation of India'
sun_df['company'] = 'Sun Pharmaceutical'
tatam_df['company'] = 'Tata Motors'
tcs_df['company'] = 'Tata Consultancy Services'
ulttech_df['company'] = 'UltraTech Cement'
upl_df['company'] = 'United Phosphorus Limited'
wipro_df['company'] = 'Wipro'

# %%
df_stocks = pd.concat([adani_df, appolo_df, asian_df, airtel_df, bajaj_df, divis_df, drreddy_df, infy_df, hind_df, hdfc_df, 
hul_df, itc_df, lt_df, mm_df, nestle_df, ongc_df, power_df, sbi_df, sun_df, rel_df, tatam_df, tcs_df, ulttech_df, upl_df, wipro_df], axis=0)

# %%
df = []
for company in df_stocks['company'].unique():
    company_df = df_stocks[['volume', 'close']][df_stocks['company'] == company]
    company_df[f'{company}_dollar_volume'] = company_df['volume'] * company_df['close']
    company_df = company_df[[f'{company}_dollar_volume']]
    df.append(company_df)
df = pd.concat(df, axis = 1)

# %%
company_df = df_stocks[['volume', 'close', 'company']]
company_df['dollar_volume'] = company_df['volume'] * company_df['close']

# %%
d= []
for company in df_stocks['company'].unique():
    monthly_volume = pd.DataFrame()
    monthly_dv = company_df['dollar_volume'][company_df['company']==company].resample('M').sum()
    monthly_v = company_df['volume'][company_df['company']==company].resample('M').sum()
    monthly_close = company_df['close'][company_df['company']==company].resample('M').mean()
    monthly_volume['dollar_volume'] = monthly_dv
    monthly_volume['volume'] = monthly_v
    monthly_volume['close'] = monthly_close
    monthly_volume['date'] = monthly_dv.index 
    monthly_volume['company'] = company
    d.append(monthly_volume)
d = pd.concat(d)
d['company'].unique()

# %%
sectors = pd.read_csv('Data\sectors.csv')

# %%
s = []
for c in d['company']:
    s.append(sectors['sector'][sectors['company']==c])
s = pd.concat(s)
d['sector'] = list(s)

# %%
fig = px.scatter(d, x="close", y="volume", animation_frame="date", animation_group="company", template='plotly_white',
                 size='dollar_volume',color="sector", hover_name="company", size_max=60, log_y=True, log_x=True, range_x=[60,21000], range_y=[250000,5994900000])
fig.update_layout(
    title='Sectorwise Volume Data',
    title_x=0.44,
    yaxis_title='Volume',
    xaxis_title='Price',
    height=600,
    # width=1200,
    )

x_avg = d['close'].mean()
y_avg = d['volume'].mean()

fig.add_vline(x=x_avg, line_width=1, opacity=0.9)
fig.add_hline(y=y_avg, line_width=1, opacity=1)

fig.add_annotation(dict(font=dict(color="black",size=14),
                        x=0, y=-0.14,#data['score'].min()-0.2, y=data['wgt'].min()-0.2,
                        text="Low Volume - Low Price",
                        xref='paper',
                        yref='paper', 
                        showarrow=False))
fig.add_annotation(dict(font=dict(color="black",size=14),
                        x=1, y=-0.14,#x=data['score'].max(), y=data['wgt'].min(),
                        text="Low Volume - High Price",
                        xref='paper',
                        yref='paper',
                        showarrow=False))
fig.add_annotation(dict(font=dict(color="black",size=14),
                        x=0, y=1.07, #x=data['score'].min(), y=data['wgt'].max(),
                        text="High Volume - Low Price",
                        xref='paper',
                        yref='paper',
                        showarrow=False))
fig.add_annotation(dict(font=dict(color="black",size=14),
                        x=1, y=1.07, #x=data['score'].max(), y=data['wgt'].max(),
                        text="High Volume - High Price",
                        xref='paper',
                        yref='paper',
                        showarrow=False))

fig.show()

plotly.offline.plot(fig, filename='scatterplot.html')
# %%
