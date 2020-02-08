class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LL:
    def __init__(self):
        self.head = None
    def swap_adj(self):
        temp = self.head
        while(temp is not None and temp.next is not None):
            temp.data, temp.next.data = temp.next.data, temp.data
            temp = temp.next.next

    def print_LL(self):
        temp = self.head
        while(temp):
            print(temp.data,end=" ")
            temp = temp.next

if __name__=='__main__':
    llist = LL()
    llist.head = Node(1)
    second = Node(2)
    third = Node(3)
    four = Node(4)
    five = Node(5)
    six = Node(6)
    llist.head.next = second
    second.next = third
    third.next = four
    four.next = five
    five.next = six
    six.next = None
    llist.swap_adj()
    llist.print_LL()


