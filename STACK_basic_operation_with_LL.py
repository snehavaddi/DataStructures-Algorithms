class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class stack:
    def __init__(self):
        self.head = None
    def push(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    def isEmpty(self):
        return True if self.head is None else False
    def pop(self):
        self.head = self.head.next

    def print_stack(self):
        temp = self.head
        while(temp):
            print(temp.data,end=" ")
            temp = temp.next

stack1 = stack()
stack1.push(10)
stack1.push(20)
stack1.push(30)
stack1.push(40)
stack1.push(50)
stack1.push(60)
print("before pop:")
stack1.print_stack()
stack1.pop()
print("after pop")
stack1.print_stack()

