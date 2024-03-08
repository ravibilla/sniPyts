# Visualize a linear relationship
# !pip install plotly-express
# !pip install seaborn
import pandas as pd
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt 
import seaborn as sns

df = pd.read_csv("https://raw.githubusercontent.com/ravibilla/datasets/main/instagram.csv", encoding = 'latin1')
df = data.dropna()
print(data.head())

# Visualize in plotly
figure = px.scatter(data_frame=df, 
                    x = "Impressions", 
                    y = "Likes", 
                    size = "Likes", 
                    trendline = "ols", # ols = ordinary least squares
                    title = "Likes vs Impressions")
figure.show()

# Visualize in matplotlib with seaborn
plt.figure(figsize=(10, 8))
plt.style.use('fivethirtyeight')
plt.title("Likes vs Impressions")
sns.regplot(x = "Impressions", y = "Likes", data = df)
plt.show()
