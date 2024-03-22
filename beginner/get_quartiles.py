# Get quartiles
import numpy as np

np.random.seed(81)
data = np.random.randint(0, 200, 10)
print(data)
q1 = np.quantile(data, 0.25)
q2 = np.quantile(data, 0.50)
q3 = np.quantile(data, 0.75)

print(f"Quartile 1: {q1: .1f}")
print(f"Quartile 2: {q2: .1f}")
print(f"Quartile 3: {q3: .1f}")