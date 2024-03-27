# Create table
#!pip install tabulate
from tabulate import tabulate

data = [["No.", "Name", "Description", "Quantity"], [1, "iPhone15", "Apple iPhone 15", 20], [2, "iPhone16", "Apple iPhone 16", 10]]
print(tabulate(data, headers='firstrow'))