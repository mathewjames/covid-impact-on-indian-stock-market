# %%
from bs4 import BeautifulSoup
import pandas as pd
import urllib.request
BASE_URL = "https://en.wikipedia.org/wiki/NIFTY_50"

# %%
html = urllib.request.urlopen(BASE_URL).read()
soup = BeautifulSoup(html, "html.parser")

# %%
table = soup.find("table", {"id": "constituents"})

# %%
table.find_all('td')[0:4]

# %%
names = table.find_all('td')[0::3]
companies = [name.a.string for name in names]

# %%
sector_soup = table.find_all('td')[2::3]
sector_names = [name.string for name in sector_soup]
sector_names[0] = 'Diversified'
sector_names[-1] = 'Information Technology'
sectors = [sector.strip() for sector in sector_names]

s = pd.Series(sectors)
s = s.replace('Financial Services','Banking / Financial Services')
s = s.replace('Banking','Banking / Financial Services')
s = s.replace('Healthcare','Healthcare / Pharmaceuticals')
s = s.replace('Pharmaceuticals','Healthcare / Pharmaceuticals')
s = s.replace('Energy - Power','Energy')
s = s.replace('Energy - Oil & Gas','Energy')
s = s.replace('Metals','Construction')

# %%
data = {'company': companies, 'sector':s}
df = pd.DataFrame(data)
df['sector'][df['company'] == "Reliance Industries"] = 'Diversified'
df['sector'][df['company'] == "Asian Paints"] = 'Chemicals'

# %%
df.to_csv('sectors.csv', index=False)

# %%
