class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class CLL:
    def __init__(self):
        self.head = None
    def push(self,data,last_node):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            last_node = self.head
            last_node.next = last_node
        else:
            new_node.next = last_node.next
            last_node.next = new_node
        self.head = new_node
        return last_node
    def insert_list(self,data,last,after_node_data):
        new_node = Node(data)
        temp = last
        while(temp.data != after_node_data):
            temp = temp.next
        new_node.next = temp.next
        temp.next = new_node
    def insert_end(self,data,last):
        new_node = Node(data)
        last.next = new_node
        last = new_node
        last.next  = self.head

    def print_list(self):
        temp = self.head
        if self.head != None:
            while(temp.next != self.head):
                print(temp.data,end=" ")
                temp = temp.next
            print(temp.data)
clist = CLL()
last = clist.push(11,None)
last = clist.push(9,last)
last = clist.push(7,last)
last = clist.push(4,last)
last = clist.push(3,last)
clist.insert_list(5,last,4)
clist.insert_end(12,last)

clist.print_list()

