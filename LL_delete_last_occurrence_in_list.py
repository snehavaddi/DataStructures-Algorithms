class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LL:
    def __init__(self):
        self.head = None
    def push(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data,end=" ")
            temp = temp.next
    def arrange_list(self,key):
        temp = self.head
        prev = None
        x = None
        pre = None
        while(temp):
            if(temp.data == key):
                x = temp
                pre = prev
            prev = temp
            temp = temp.next
        if x != None:
            pre.next = x.next

llist = LL()
llist.push(70)
llist.push(25)
llist.push(43)
llist.push(22)
llist.push(22)
llist.push(10)
llist.arrange_list(22)

llist.printList()

