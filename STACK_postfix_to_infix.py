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

    def convert_infix(self):
        temp = self.head
        string = None
        while(temp):
            if temp.data.isalpha():
                self.stack.append(temp.data)
            else:
                for i in range(2):
                    # self.infix.append(self.pop())
                    if string != None:
                        string = string + self.pop()
                    else:
                        string = self.pop()
                    if i != 1:
                        # self.infix.append(temp.data)
                        string = string + temp.data
                    self.stack.pop()
                string = "(" + string + ")"
                self.stack.append(string)
                string = None
                self.infix.clear()
            temp = temp.next
        return self.stack[0]
stack1 = exp()
stack1.push('*')
stack1.push('-')
stack1.push('a')
stack1.push('/')
stack1.push('b')
stack1.push('c')
stack1.push('-')
stack1.push('/')
stack1.push('a')
stack1.push('k')
stack1.push('l')
# stack1.print_list()

infix = stack1.convert_infix()
print(infix)