def arr_sort(arr,n):
    arr.sort()
    start = 0
    end = n-1
    k = 0
    temp = arr[n-1]
    while (start < end):
        while (k <= end):
            if (end != k):
                arr[end] = arr[end - 1]
                end = end - 1
            else:
                arr[end] = temp
                k = k + 2
                start = start + 2
                end = n-1
                temp = arr[end]

arr = [1, 12, 4, 6, 7, 10]
n = len(arr)
arr_sort(arr,n)
print(arr)