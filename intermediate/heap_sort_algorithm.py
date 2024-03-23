# Heap sort algorithm

def maxHeapify(A, i):
    left = 2 * i  + 1
    right = 2 * i + 2
    largest = i
    if left < len(A) and A[left] > A[largest]:
        largest = left
    if right< len(A) and A[right] > A[largest]:
        largest = right
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        A = maxHeapify(A, largest)
    return A

def buildMaxHeap(A):
    for i in range(len(A)//2, -1, -1):
        A = maxHeapify(A, i)
    return A

def heapSort(A):
    n = len(A)
    if n <= 1:
        return A
    A = buildMaxHeap(A)
    for k in range(n, 0, -1):
        A[0], A[k-1] = A[k-1], A[0]
        A[:k-1] = maxHeapify(A[:k-1], 0)
    return A

A = [20, 17, 9, 10, 8, 12, 15, 3]
heapSort(A)
