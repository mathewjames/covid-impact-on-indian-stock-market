import plotly.graph_objects as go
import pandas as pd
import os

directory = r'filepath'

for filename in os.scandir(directory):
    if filename.is_file():
        base_file_name = os.path.splitext(os.path.basename(filename))[0]
        base_file_extension = os.path.splitext(os.path.basename(filename))[1]
        df = pd.read_csv(rf'{filename.path}')
        df = df.drop('Unnamed: 0', axis=1)
        date_df = df.loc[df["date"].between("2015-01-01", "2022-01-01")]
        date_df['year'] = pd.DatetimeIndex(date_df['date']).year
        date_df['month'] = pd.DatetimeIndex(date_df['date']).month_name().str.slice(stop=3)
        date_df.to_csv(rf'filepath\Processed\{base_file_name}_processed{base_file_extension}', index=False)
