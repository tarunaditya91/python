import pandas as pd

data=pd.read_html('https://en.wikipedia.org/wiki/List_of_The_Simpsons_episodes')
a=len(data)
print(data[1])