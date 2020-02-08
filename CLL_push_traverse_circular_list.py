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
    def print_list(self):
        temp = self.head
        if self.head != None:
            while(temp.next != self.head):
                print(temp.data,end=" ")
                temp = temp.next
            print(temp.data)
clist = CLL()
clist.push(5)
clist.push(4)
clist.push(3)
clist.push(2)
clist.push(1)
clist.print_list()
