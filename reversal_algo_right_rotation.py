#Reversal algorithm for right rotation of an array
def arrReversal(arr,key,length):
	rev(arr,0,length-1)
	rev(arr,0,key-1)
	rev(arr,key,length-1)
	print("final array after right rotation is:%s" % arr)

def rev(arr,start,end):
	while(start < end):
		arr[start] , arr[end] = arr[end] , arr[start]
		start = start + 1
		end = end - 1


arr = list(map(int, input("enter the input array: ").split()))
key = list(map(int, input("no of rotations: ").split()))
length = len(arr)
arrReversal(arr,key[0],length)

