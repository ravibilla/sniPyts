# Find missing numbers
def find_missing_numbers(lst):
    nums = set(lst)
    missing_nums = []
    for i in range(min(lst), max(lst)):
        if i not in nums:
            missing_nums.append(i)
    
    return missing_nums

num_list = [1, 2, 3, 5, 6, 8, 9, 10, 12, 16]    
print(f"{find_missing_numbers(num_list)}")