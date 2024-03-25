# Sequential search
def search_sequentially(lst, elm):
    found = False
    for idx in range(len(lst)):
        if lst[idx] == elm:
            found = True
            break
    if found:
        response = f"{elm} found at index: {i} in the list {lst}"
    else: 
        response =  f"{elm} not found in the list {lst}"
    return(response)
    
numbers = list(range(0, 15, 2))
print(search_sequentially(numbers, 21))