# Bubble sort algorithm
def bubble_sort(arr):
    l = len(arr)
    swapped = False
    for i in range(l-1):
        for j in range(l-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if swapped == False:
            break
    return(arr)

my_list = [0, 64, 34, 25, 12, 22, 11, 1]
sorted_list = bubble_sort(my_list)
print("Sorted list:", sorted_list)