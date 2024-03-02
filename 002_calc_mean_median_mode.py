# Calculate mean, median and mode
import random

# Mean
list = [random.randrange(10, 30) for i in range(10)]
mean = sum(list)/len(list)
print(f"Mean of {list}: {mean}")

# Median 
list = [random.randrange(10, 30) for i in range(10)]
list.sort()
if len(list) % 2 == 0:
    m1 = list[len(list)//2]
    m2 = list[len(list)//2 - 1]
    median = (m1 + m2)/2
else:
    median = list[len(list)//2]
print(f"Median of {list}: {median}")

# Mode
list = [12, 16, 20, 20, 12, 30, 25, 23, 24, 20]
frequency = {}
for i in list:
    frequency.setdefault(i, 0)
    frequency[i] += 1

frequent = max(frequency.values())
for i, j in frequency.items():
    if j == frequent:
        mode = i
print(f"Mode of {list}: {mode}")

# Mode: Simple with dictionary comprehension
list = [12, 16, 20, 20, 12, 30, 25, 23, 24, 20]
freq = {key: list.count(key) for key in list} 
mode = max(freq, key=freq.get)
print(f"Mode of {list}: {mode}")
