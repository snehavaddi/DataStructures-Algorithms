class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class CLL:
    def __init__(self):
        self.head = None
    def push(self,data):
        new_node = Node(data)
        new_node.next = self.head
        if self.head != None:
            temp = self.head
            while (temp.next != self.head):
                temp = temp.next
            temp.next = new_node
        else:
            new_node.next = new_node
        self.head = new_node
    def insert(self,data):
        new_node = Node(data)
        temp = self.head
        if self.head == None:
            new_node.next = self.head
            self.head = new_node
        if self.head != None :
            while temp.data < data and temp.next != self.head:
                prev = temp
                temp = temp.next
            if temp == self.head:
                temp.data,new_node.data = new_node.data,temp.data
                next = temp.next
                temp.next = new_node
                new_node.next = next
            elif temp.next == self.head:
                temp.next = new_node
                new_node.next = self.head
            else:
                new_node.next = prev.next
                prev.next = new_node

    def print_list(self):
        temp = self.head
        if self.head != None:
            while(temp.next != self.head):
                print(temp.data,end=" ")
                temp = temp.next
            print(temp.data)
clist = CLL()
clist.push(11)
clist.push(9)
clist.push(7)
clist.push(4)
clist.push(3)

clist.insert(8)
clist.insert(2)
clist.insert(12)
clist.insert(0)
clist.print_list()

