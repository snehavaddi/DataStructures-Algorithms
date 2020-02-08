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
    def split_list(self,clist1,clist2):
        slow_ptr = self.head
        fast_ptr = self.head
        if self.head == None:
            return None
        if self.head != None:
            temp = self.head
            while(fast_ptr.next != self.head and fast_ptr.next.next != self.head):
                fast_ptr = fast_ptr.next.next
                slow_ptr = slow_ptr.next
            if fast_ptr.next.next == self.head:
                fast_ptr = fast_ptr.next
            clist1.head = temp
            clist2.head = slow_ptr.next
            fast_ptr.next = clist2.head
            slow_ptr.next = clist1.head

    def print_list(self):
        temp = self.head
        if self.head != None:
            while(temp.next != self.head):
                print(temp.data,end=" ")
                temp = temp.next
            print(temp.data)
clist = CLL()
clist1 = CLL()
clist2 = CLL()
clist.push(5)
clist.push(4)
clist.push(3)
clist.push(2)
clist.push(1)
clist.split_list(clist1,clist2)
clist.print_list()
clist1.print_list()
clist2.print_list()

