# Least common multiple
def least_common_multiple(a, b):
    max_val = max(a,b)
    while True: 
        if (max_val % a == 0) and (max_val % b == 0):
            lcm = max_val 
            break
        max_val += 1
    return lcm

least_common_multiple(3, 7)