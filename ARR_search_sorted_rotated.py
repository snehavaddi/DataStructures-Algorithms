def find_pivot(arr,key,n):
    for i in range(n):
        if i == n-1:
            print("element to be search is at index:%d" % (key-1))
            exit()
        if arr[i] > arr[i+1]:
            pivot = arr[i]
            break

    for i in range(n):
        if key > arr[i]:
            search_sorted_array(arr,0,pivot-1,key)
        if key < arr[i]:
            search_sorted_array(arr,pivot,n-1,key)
        if key == arr[i]:
            print("element found at index:%d" % i)
            break

def search_sorted_array(arr,start,end,key):
    for i in range(end):
        if key == arr[i]:
            print("element found at index:%d" % i)
            exit()



arr =  list(map(int, input("enter the input array: ").split()))
key =  list(map(int, input("enter the key to search: ").split()))
n = len(arr)
find_pivot(arr,key[0],n)