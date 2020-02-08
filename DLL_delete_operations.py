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
    def delete_front(self):
        self.head = self.head.next
        self.head.prev = None
    def delete_after(self,after_node):
        after_node.next = after_node.next.next
        after_node.next.prev = after_node
    def delete_before(self,before_node):
        before_node.prev = before_node.prev.prev
        before_node.prev.next = before_node
    def delete_last(self,last_node):
        last_node.prev.next = None
        last_node.prev = None
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

dllist.delete_front()
dllist.delete_after(second)
dllist.delete_before(five)
dllist.delete_last(five)
dllist.printlist()