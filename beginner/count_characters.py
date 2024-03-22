# Count Characters
def count_characters(str):
    count = {}
    for c in str:
        if c in count:
            count[c] += 1
        else: 
            count[c] = 1
    return count

print(count_characters("Let's count characters in string!"))
