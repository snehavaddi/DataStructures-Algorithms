class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
class exp:
    def __init__(self):
        self.head = None
        self.stack = []
        self.infix = []
        self.preced = {"+" : 1, "-" : 1, "*" : 2, "/" : 2, "(" : 3, ")" : 3}
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
            print(temp.data,end="")
            temp = temp.next
    def peek(self):
        return self.stack[-1]
    def pop(self):
        return self.stack[-1]
    def check_balance(self):
        temp = self.head
        while(temp):
            x = temp.data
            self.stack.append(x)
            prev = temp
            temp = temp.next

stack1 = exp()
stack1.push('}')
stack1.push(')')
stack1.push('(')
stack1.push(']')
stack1.push(')')
stack1.push('(')
stack1.push(')')
stack1.push('(')
stack1.push('[')
stack1.push('{')
stack1.print_list()

# infix = stack1.convert_infix()
# print(infix)