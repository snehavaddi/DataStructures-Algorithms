class Node:
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None

class DLL:
    def __init__(self):
        self.head = None
    def printlist(self):
        temp = self.head
        while(temp):
            print(temp.data,end=" ")
            temp = temp.next
    def reverse(self):
        curr = self.head
        prev = None
        next  = None
        while(curr):
            next = curr.next
            curr.next = prev
            curr.prev = next
            prev = curr
            curr = next
        self.head = prev

dllist = DLL()
dllist.head = Node(1)
second = Node(2)
third = Node(3)
fourth = Node(4)
five = Node(5)
dllist.head.next = second
second.next = third
second.prev = dllist.head
third.prev = second
third.next = fourth
fourth.prev = third
fourth.next = five
five.prev = fourth

dllist.reverse()

dllist.printlist()