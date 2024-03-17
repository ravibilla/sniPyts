# Find min index
a = [23, 76, 45, 20, 76, 65, 15, 54]
min_idxs = []

for idx, elm in enumerate(a):
    if elm == min(a):
        min_idxs.append(idx)
    
print(min_idxs)