# %%
import plotly.express as px
import plotly
import plotly.graph_objects as go
import pandas as pd

# %%
df = pd.read_csv(r"Data\demat_accounts.csv")

# %%
x = df['Period']
y = df['New Demat Accounts (millions)']

# %%
fig = go.Figure(data=[go.Bar(x=x, y=y,
            hovertext=['20.4 million new accounts', '25 million new accounts', '41 million new accounts', '40 million new accounts', '50 million new accounts', '142 million new accounts', '346 million new accounts'])])
# Customize aspect
fig.update_traces(marker_color='rgb(158,202,225)', marker_line_color='rgb(8,48,107)',
                  marker_line_width=1.5, opacity=0.6)
fig.update_layout(title_text='New Investors', title_x=0.5, yaxis_title='New Demat Accounts (millions)', xaxis_title='Period',)
fig.update_layout(template='plotly_white')

fig.show()
plotly.offline.plot(fig, filename='bar.html')
