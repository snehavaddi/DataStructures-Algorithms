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
    def clone_list(self,list):
        self.copy_node(list)
        self.random_link(list)
        clone_curr = self.restore_lists(list)
        return clone_curr

    def copy_node(self,list):
        curr = self.head
        while (curr):
            clone_node = Node(curr.data)
            clone_node.next = curr.next
            curr.next = clone_node
            curr = curr.next.next
    def random_link(self,list):
        curr = self.head
        while(curr):
            curr.next.random = curr.random.next
            curr = curr.next.next
    def restore_lists(self,list):
        curr = self.head
        clone_curr = self.head.next
        while(curr.next):
            tmp = curr.next
            curr.next = curr.next.next
            curr = tmp
        return clone_curr
dllist = DLL()
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
clone_curr = dllist.clone_list(dllist)
print("cloned list is:")
dllist.printlist_clone(clone_curr)
