class Node:
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None

class DLL:
    def __init__(self):
        self.head = None
        self.head1 = None
        self.last = None
    def printlist(self):
        temp = self.head1
        while(temp):
            print(temp.data,end=" ")
            temp = temp.next
    def push_front(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head.prev = new_node
        new_node.prev = None
        self.head = new_node
    def insert_after(self,prev_node,data):
        new_node = Node(data)
        new_node.next = prev_node.next
        new_node.prev = prev_node
        prev_node.next = new_node
    def insert_before(self,next_node,data):
        new_node = Node(data)
        new_node.prev = next_node.prev
        new_node.next = next_node
        next_node.prev = new_node
        new_node.prev.next = new_node
    def insert_last(self,last_node,data):
        new_node = Node(data)
        last_node.next = new_node
        new_node.prev = last_node
        new_node.next = None
    def find_len(self):
        temp = self.head
        count = 0
        while(temp):
            count = count + 1
            temp = temp.next
        return count
    def rotate_right(self,k,l):
        temp = self.head
        c = l - k
        while(temp.next):
            if(l == c):
                self.head1 = temp
                temp.prev.next = None
                temp.prev = None
            l = l - 1
            temp = temp.next
        temp.next = self.head
        self.head.prev = temp

dllist = DLL()
dllist.head = Node(1)
second = Node(2)
third = Node(3)
fourth = Node(4)
five = Node(5)
dllist.head.next = second
second.next = third
second.prev = dllist.head
third.prev = second
third.next = fourth
fourth.next = five
fourth.prev = third
k = 3
l = dllist.find_len()
dllist.rotate_right(k,l)
dllist.printlist()