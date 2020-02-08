class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class LL:
    def __init__(self):
        self.head = None
    def push(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    def decimal_sum(self):
        sum = 0
        curr = self.head
        while(curr):
            sum = sum*2 + curr.data
            curr = curr.next
        print(sum)
    def print_list(self):
        temp = self.head
        while(temp):
            print(temp.data, end=' ')
            temp = temp.next

llist = LL()
llist.push(1)
llist.push(0)
llist.push(0)
llist.push(0)
llist.push(1)
llist.push(0)

llist.decimal_sum()
#llist.print_list()




