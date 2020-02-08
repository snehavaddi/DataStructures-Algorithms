class Node:
    def __init__(self, x,y):
        self.x = x
        self.y = y
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None

    def push(self,x,y):
        new_node = Node(x,y)
        if self.head == None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def delete_list(self):
        temp = self.head
        final = self.head
        prev = None
        while(temp.next):
            if temp == self.head:
                prev = temp
                temp = temp.next
                continue
            if temp.y == temp.next.y:
                prev.next = temp.next
                temp = temp.next
                continue
            if temp.y != temp.next.y:
                prev = temp.next
                temp = temp.next.next
                continue
            prev = temp
            temp = temp.next

    def printList(self):
        temp = self.head
        while (temp):
            print(temp.x,temp.y,end=" ")
            temp = temp.next

llist = LinkedList()
llist.push(2,3)
llist.push(4,3)
llist.push(6,3)
llist.push(10,3)
llist.push(12,3)


llist.delete_list()

llist.printList()