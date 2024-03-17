# Count frequent words
words = []
with open("./files/sample.txt", "r") as f:
    for line in f:
        words.extend(line.split())

from collections import Counter
counts = Counter(words)
top_5 = counts.most_common(5)
print(top_5)