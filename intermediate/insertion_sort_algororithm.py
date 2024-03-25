# Insertion sort algorithm
def insertion_sort(A):
    for i in range(len(A)-1):
        if A[i] > A[i+1]:
            A[i], A[i+1] = A[i+1], A[i]
            for j in range(i, 0, -1):
                if A[j] < A[j-1]:
                    A[j], A[j-1] = A[j-1], A[j]
    return A

A =[14, 3, 2, 10, 12, 1, 5, 6]
print(insertion_sort(A))