# Scrape table from website 
import urllib.request
import pandas as pd

url = "https://en.wikipedia.org/wiki/Large_language_model"

with urllib.request.urlopen(url) as i:
    html  = i.read()

data =  pd.read_html(html)[2]
print(data.head())
#data.to_csv("llms.csv")