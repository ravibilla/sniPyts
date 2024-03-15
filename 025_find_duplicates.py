# Find duplicates
def find_duplicats(items):
    dups = []
    for item in items:
        item_cnt = 0
        for i in range(len(items)):
            if items[i] == item:
                item_cnt += 1
        if item_cnt > 1 and item not in dups:
            dups.append(item)
    return dups

list = ["Ravi", "Billa", "Ravi", "Billa", "Babu"]
find_duplicats(list)