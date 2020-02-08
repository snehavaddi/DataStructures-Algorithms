class Node:
    def __init__(self,data):
        self.data = data
        self.random = None
        self.next = None

class DLL:
    def __init__(self):
        self.head = None
    def printlist(self):
        temp = self.head
        while(temp):
            print("data:%d" % temp.data,end=", ")
            print("random data:%d" % temp.random.data,end=" ")
            print("\r")
            temp = temp.next
    def printlist_clone(self,clone_curr):
        temp = clone_curr
        while(temp):
            print("data:%d" % temp.data,end=", ")
            print("random data:%d" % temp.random.data,end=" ")
            print("\r")
            temp = temp.next
    def copy(self,list_copy):
        curr = self.head
        curr_copy = list_copy.head
        while(curr):
            if list_copy.head == None:
                new_node = Node(curr.data)
             #   new_node.next = list_copy.head
                list_copy.head = new_node
                prev = new_node
            else:
                new_node = Node(curr.data)
                prev.next = new_node
                prev = new_node
            curr = curr.next
        return list_copy
    def next_ptr(self,list_copy):
        curr = self.head
        curr_copy = list_copy.head
        while(curr):
            nxt = curr.next
            curr_copy.random = curr
            curr.next = curr_copy
            curr = nxt
            curr_copy = curr_copy.next
        return dllist
    def set_random(self,org_list):
        org_curr = org_list.head
        copy_curr = self.head
        while(copy_curr):
            copy_curr.random = copy_curr.random.random.next
            copy_curr = copy_curr.next

dllist = DLL()
dllist_copy = DLL()
dllist.head = Node(1)
second = Node(2)
third = Node(3)
fourth = Node(4)
five = Node(5)
dllist.head.next = second
dllist.head.random = third
second.next = third
second.random = dllist.head
third.random = five
third.next = fourth
fourth.random = third
fourth.next = five
five.random = second
five.next = None
print("original list is:")
dllist.printlist()
list_copy = dllist.copy(dllist_copy)
dllist.next_ptr(list_copy)
dllist_copy.set_random(dllist)
print("copy list is:")
dllist_copy.printlist()