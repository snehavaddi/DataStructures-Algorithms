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
    def next_greater(self):
        temp = self.head
        while(temp):
            if len(self.stack) == 0 :
                self.stack.append(temp.data)
            else:
                if self.stack[-1] < temp.data:
                    while(len(self.stack)!= 0):
                        print("greater element for" ,self.stack[-1] ,"is:",  temp.data )
                        self.stack.pop()
                    self.stack.append(temp.data)
                    if temp.next == None:
                        print("greater element for", self.stack[-1], "is:", -1)
                else:
                    self.stack.append(temp.data)
            temp = temp.next
stack1 = exp()
stack1.push(25)
stack1.push(2)
stack1.push(5)
stack1.push(4)
stack1.print_list()

stack1.next_greater()

# infix = stack1.convert_infix()
# print(infix)