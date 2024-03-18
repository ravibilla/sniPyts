# Calculate code execution time
from time import time
import numpy as np

start = time()
# Sample matrix mulitplication code
a = np.random.randint(10, size=(10, 10))
b = np.random.randint(10, size=(10, 10))
c = np.matmul(a, b)
print(c)
end = time()

print(f"Code executioin time: {round((end - start)*1000, 2)} ms")
