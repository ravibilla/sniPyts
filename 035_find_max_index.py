# Find max index
a = [23, 76, 45, 20, 76, 65, 15, 54]
max_idxs = []

for idx, elm in enumerate(a):
    if elm == max(a):
        max_idxs.append(idx)
    
print(max_idxs)