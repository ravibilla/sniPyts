# Binary search algorithm
def binary_search(arr, low, high, elm):
    
    # Check base case
    if high >= low:

        mid = (low + high) // 2
        # Check if the element is present in the middle of the array
        if arr[mid] == elm:
            return mid

        # Check if the element is present in the left part of the array
        elif arr[mid] > elm:
            return binary_search(arr, low, mid-1, elm)

        # Check if the element is present in the right part of the array
        elif arr[mid] < elm:
            return binary_search(arr, mid+1, high, elm)
    else:
        return -1

numbers = [2, 4, 8, 11, 13, 30, 40]
elm = 13
idx = binary_search(numbers, 0, 6, elm)
if idx == -1:
    print(f"Cannot find {elm} in the array")
else:
    print(f" Found {elm} at index:{idx} in the array")