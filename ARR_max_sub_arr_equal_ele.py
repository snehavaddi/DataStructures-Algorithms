def find_arr(A,n):
    count = 1
    temp = n
    counter = 0
    for i in range(n-1):
        if A[i] == A[i+1]:
            count = count + 1
            if count == temp:
                sub_arr_len = temp * 2
            continue
        if A[i] != A[i+1]:
            counter = counter + 1
            if temp > count:
                temp = count
                count = 1
            if counter == 2:
                sub_arr_len = temp * 2
                counter = 0
                if temp <  count:
                    temp = count
                    count = 1
    return sub_arr_len

A = [1,2,1,2,1,2,2,1,1]
n = len(A)
final = find_arr(A,n)
print(final)