class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class DLL:
    def __init__(self):
        self.head = None
    def printlist(self):
        temp = self.head
        while(temp):
            print(temp.data,end=" ")
            temp = temp.next
    def find_len(self):
        temp = self.head
        length = 0
        while(temp):
            temp = temp.next
            length = length + 1
        return length
    def swap(self,k,l):
        node_x = self.head
        prev_x = None
        prev_y = None
        count = 1
        while(count < k):
            prev_x = node_x
            node_x = node_x.next
            count = count + 1
        node_y = self.head
        count = 1
        while(count < l-k+1):
            prev_y = node_y
            node_y = node_y.next
            count = count + 1
        prev_x.next = node_y
        prev_y.next = node_x
        temp = node_x.next
        node_x.next = node_y.next
        node_y.next = temp

dllist = DLL()
dllist.head = Node(1)
second = Node(2)
third = Node(3)
fourth = Node(4)
five = Node(5)
six = Node(6)
seven = Node(7)
dllist.head.next = second
second.next = third
third.next = fourth
fourth.next = five
five.next = six
six.next = seven
print("original list is:")
dllist.printlist()
k = 3
l = dllist.find_len()
dllist.swap(k,l)
dllist.printlist()
