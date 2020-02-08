def find_flips(arr,n):
    f = []
    while(n):
        max,index = find_large(arr,n)
        f.append(index+1)
        f.append(n)
        k = 0
        while(k<int((index+1)/2)):
            temp = arr[k]
            arr[k] = arr[index]
            arr[index] = temp
            k = k + 1
        l = 0
        p = n-1
        while(l<int(n/2)):
            temp = arr[l]
            arr[l] = arr[p]
            arr[p] = temp
            l = l + 1
            p = p - 1
        n = n - 1
    return f , arr


def find_large(arr,n):
    index = 0
    max = arr[0]
    j = 0
    for j in range(n-1):
        if max < arr[j+1]:
            max = arr[j+1]
            index = j+1
    return max,index

arr=  [3,2,4,1]
f = []
f , arr= find_flips(arr,len(arr))
for i in f:
    print(i,end=" ")
print('/n')
for j in arr:
    print(j,end=" ")