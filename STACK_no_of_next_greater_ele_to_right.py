class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
class exp:
    def __init__(self):
        self.head = None
        self.stack = []

    def push(self,item):
        new_node = Node(item)
        if self.head == None:
            new_node.next = self.head
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
    def print_list(self):
        temp = self.head
        while(temp):
            print(temp.data,end=" ")
            temp = temp.next
    def nge_right(self,index):
        max = index
        temp = self.head
        c = 0
        count = 0
        while(c != index ):
            temp = temp.next
            c = c + 1
        self.stack.append(temp.data)
        while(temp):
            if self.stack[0] < temp.data:
                self.stack.pop()
                self.stack.append(temp.data)
                count = count + 1
            temp = temp.next
        self.stack.pop()
        return count

stack1 = exp()
stack1.push(6)
stack1.push(10)
stack1.push(8)
stack1.push(5)
stack1.push(7)
stack1.push(2)
stack1.push(4)
stack1.push(3)
stack1.print_list()

c = stack1.nge_right(0)
print(c)
c = stack1.nge_right(5)
print(c)

