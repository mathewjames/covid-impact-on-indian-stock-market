# %%
import plotly.express as px
import plotly
import plotly.graph_objects as go
import pandas as pd
from plotly.subplots import make_subplots

# %%
sectors = pd.read_csv('Data\sectors.csv')
counts = sectors['sector'].value_counts()
a = sectors.groupby('sector').count()

# %%
a.reset_index(inplace=True)
a

# %%
a['sector'][a['company'] == 1] = 'Others'
b = a.groupby('sector').count()
b.reset_index(inplace=True)
c = int(b['company'][b['sector'] == 'Others'])
a['company'][a['sector']=='Others'] = c
a = a.drop_duplicates()

# %%
labels = a.sector
values = a.company
colors = ['blue', 'red', 'yellow', 'lightgreen']
# Create subplots: use 'domain' type for Pie subplot
fig = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.3)])
fig.update_traces(hoverinfo="label+value", textinfo='label+percent', textposition='outside')

fig.update_layout(
    title_text="Nifty 50 Sector Weightage", title_x=0.5,
    # width=1000,
    # Add annotations in the center of the donut pies.
    annotations=[dict(text='Sectors', x=0.5, y=0.5, font_size=15, showarrow=False),
                 ])
fig.show()
plotly.offline.plot(fig, filename='pie.html')
