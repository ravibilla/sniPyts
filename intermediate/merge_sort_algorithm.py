# Merge sort algorithm
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    # Divide the array into two halves
    mid = len(arr)//2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Recursively sort both halves
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    # Merge the sorted halves
    return merge_arr(left_half, right_half)


def merge_arr(left, right):
    merged = []
    left_index, right_index = 0, 0

    # Compare elements from both halves and add the smaller to the merged list
    while(left_index < len(left) and right_index < len(right)):
        if left[left_index] < right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    # Add any remaining elements from the left and right halves (if any)
    merged.extend(left[left_index:])
    merged.extend(right[right_index:])

    return merged

my_list = [0, 64, 34, 25, 12, 22, 11, 1]
sorted_list = merge_sort(my_list)
print("Sorted list:", sorted_list)