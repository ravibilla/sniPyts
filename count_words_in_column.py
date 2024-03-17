# Count number of words in a column
import pandas as pd

data = pd.read_csv("https://raw.githubusercontent.com/ravibilla/datasets/main/titanic.csv", encoding='latin1')
print(data.head())

data['# Words'] = data["Name"].apply(lambda x: len(x.split()))
print(data[['Name', '# Words']])