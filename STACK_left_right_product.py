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
    def LRproduct(self):
        temp = self.head
        prev = temp
        temp = temp.next
        count = 1
        while(temp):
            count = count + 1
            if temp.data < prev.data and temp.data < temp.next.data:
                product = (count - 1) * (count + 1)
                return product
            else:
                prev = temp
                temp = temp.next


stack1 = exp()
# stack1.push(6)
# stack1.push(10)
# stack1.push(8)
stack1.push(5)
stack1.push(4)
stack1.push(3)
stack1.push(4)
stack1.push(5)
# stack1.print_list()

p = stack1.LRproduct()
print(p)

