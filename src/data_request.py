import pandas as pd
import requests


class TurbineData:
    def __init__(self, url="https://run.mocky.io/v3/6a13fe7e-840c-4d82-b58f-c737139f0e55"):
        self.url = url
        self.data = pd.DataFrame()
        self.formatted_data = None
        self.error = None

        if self.url:
            self.fetch_data()
        if not self.data.empty:
            self.format_data()
  
    def fetch_data(self):
        try:
            r = requests.get(self.url)
            r.raise_for_status()
            self.data = pd.DataFrame(r.json())
        except requests.exceptions.HTTPError as err:
            self.error = err

    def format_data(self):
        self.formatted_data = pd.DataFrame()
        for index, row in self.data.iterrows():
            print('LEVEL {}: {}'.format(row['level'], row))
            self.formatted_data.loc[row['turbine'], 'Name'] = row['turbine']
            if row['level'] == 1:
                level = 'WARNING'
            elif row['level'] == 2:
                level = 'CRITICAL'
            self.formatted_data.loc[row['turbine'], level] = row['count']
        self.formatted_data = self.formatted_data.fillna(0)
        self.formatted_data = self.formatted_data.sort_values(['WARNING'], ascending=[False])
        self.formatted_data = self.formatted_data.sort_values(['CRITICAL'], ascending=[False])
        print(self.formatted_data)
