import pandas as pd

data=pd.read_csv('https://www.football-data.co.uk/mmz4281/2324/E0.csv')
print(data)
print(data[1:5])

data.rename(columns={'HomeTeam':'HT',
                     'AwayTeam':'AT'},inplace=True)
print(data)