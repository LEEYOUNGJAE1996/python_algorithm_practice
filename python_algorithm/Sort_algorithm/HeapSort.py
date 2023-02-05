def heapify(arr, n, i):
    largest = i
    # 자식 노드 표현
    l = 2 * i + 1
    r = 2 * i + 2
    print(l, " ", n, "  ", r)

    if l < n and arr[i] < arr[l]:
        largest = l
    if r < n and arr[largest] < arr[r]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        print("heapify 2: ", arr)
        heapify(arr, n, largest)


def heapSort(arr):
    n = len(arr)

    for i in range(n, -1, -1):
        print("first for : ", arr, " ", i)
        heapify(arr, n, i)
    for i in range(n-1, 0, -1):
        print("second for : ", arr, " ", i)
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)


arr = [12, 11, 13, 5, 6, 7]
heapSort(arr)
print("Sorted array : ", arr)
