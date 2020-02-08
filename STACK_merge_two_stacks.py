class Node:
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None
class stack:
    def __init__(self):
        self.head = None
        self.lastnode = None

    def push(self,item):
        new_node = Node(item)
        if self.head != None:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
            self.lastnode = self.head
    def pop(self):
        x = self.head
        self.head = self.head.next
        return x
    def merge(self,stack2):
        self.lastnode.next = stack2.head
    def print_list(self):
        temp = self.head
        while(temp):
            print(temp.data,end=" ")
            temp = temp.next

stack1 = stack()
stack2 = stack()
stack1.push(4)
stack1.push(3)
stack1.push(2)
stack1.push(1)

stack2.push(8)
stack2.push(7)
stack2.push(6)
stack2.push(5)

stack1.merge(stack2)
stack1.print_list()



