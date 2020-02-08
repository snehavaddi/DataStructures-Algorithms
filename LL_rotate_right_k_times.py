class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def rotate_right(self,k):
        temp = self.head
        while(temp):
            if temp.next == None:
                while(k):
                    node = Node(self.head.data)
                    if self.head.next is not None:
                        self.head = self.head.next
                    temp.next = node
                    node.next = None
                    k  = k - 1
                    temp = temp.next
            temp = temp.next

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data,end=" ")
            temp = temp.next

llist = LinkedList()
llist2 = LinkedList()
llist3 = LinkedList()
llist.push(7)
llist.push(6)
llist.push(5)
llist.push(4)
llist.push(3)
llist.push(2)
llist.push(1)

llist.rotate_right(4)

llist.printList()