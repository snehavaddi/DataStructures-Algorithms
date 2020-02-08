def findmax(arr,length):
    count_o = 0
    count_l = 0
    count_o_max = 0
    count_l_max = 0
    for i in range(length):
        if arr[i] == 1:
            if(count_o_max < count_o):
                count_o_max = count_o
            count_o = 0
            count_l = count_l + 1
        else:
            if(count_l_max < count_l):
                count_l_max = count_l
            count_l = 0
            count_o = count_o + 1
    if (count_o_max < count_o):
        count_o_max = count_o
    if (count_l_max < count_l):
        count_l_max = count_l
    if(count_l_max > count_o_max):
        print("maximum count is for 1s:",count_l_max)
    else:
        print("maximum count is for 0s:", count_o_max)

arr = [0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
length = len(arr)
findmax(arr,length)