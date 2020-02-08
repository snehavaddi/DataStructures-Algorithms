class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class CLL:
    def __init__(self):
        self.head = None
    def push(self,data):
        new_node = Node(data)
        new_node.next = self.head
        if self.head != None:
            temp = self.head
            while (temp.next != self.head):
                temp = temp.next
            temp.next = new_node
        else:
            new_node.next = new_node
        self.head = new_node
    def print_list(self):
        temp = self.head
        if self.head != None:
            while(temp.next != self.head):
                print(temp.data,end=" ")
                temp = temp.next
            print(temp.data)
    def find_position(self,m):
        ptr = self.head
        fast_ptr = self.head
        temp = 1
        while(fast_ptr.next != fast_ptr):
            if temp == m:
                temp = 1
                prev.next = fast_ptr.next
            else:
                prev = fast_ptr
                fast_ptr = fast_ptr.next
                temp = temp + 1
        return fast_ptr.data
clist = CLL()
#clist.push(5)
clist.push(4)
clist.push(3)
clist.push(2)
clist.push(1)
m = 2
final = clist.find_position(m)
print(final)
#clist.print_list()
