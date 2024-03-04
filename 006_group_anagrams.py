# Group anagrams
from collections import defaultdict

def group_anagrams(words):
    dfdict = defaultdict(list)
    for w in words:
        sorted_word = "".join(sorted(w))
        dfdict[sorted_word].append(w)
    return dfdict.values()

words = ["tea", "eat", "bat", "ate", "arc", "car"]
print(f"Grouped anagrams: {group_anagrams(words)}")
