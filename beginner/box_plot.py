# Box plot
import pandas as pd
import plotly_express as px
iris = pd.read_csv("https://gist.githubusercontent.com/netj/8836201/raw/6f9306ad21398ea43cba4f7d537619d0e07d5ae3/iris.csv")
print(iris.head())

plt = px.box(iris, y=["sepal.length", "sepal.width", "petal.length", "petal.width"])
plt.show()