def form_wave(arr,n):
    count = 0
    for i in range(n-1):
        if arr[i] > arr[i+1]:
            if count % 2 == 0:
                arr[i], arr[i+1]= arr[i+1], arr[i]
                count = count + 1
                continue
            if count % 2 == 1:
                count = count + 1
        else:
            count = count + 1


arr = [64, 25, 12, 22, 11, 1,2,44,3,122, 23, 34]
n = len(arr)
form_wave(arr,n)
print(arr)

# second Method:
# Python function to sort the array arr[0..n-1] in wave form,
# i.e., arr[0] >= arr[1] <= arr[2] >= arr[3] <= arr[4] >= arr[5]
def sortInWave(arr, n):
    # sort the array
    arr.sort()

    # Swap adjacent elements
    for i in range(0, n - 1, 2):
        arr[i], arr[i + 1] = arr[i + 1], arr[i]

    # Driver progrM


arr = [10, 90, 49, 2, 1, 5, 23]
sortInWave(arr, len(arr))
for i in range(0, len(arr)):
    print
    arr[i],

# This code is contributed by __Devesh Agrawal__
