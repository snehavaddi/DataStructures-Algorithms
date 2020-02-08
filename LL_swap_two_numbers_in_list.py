class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LL:
    def __init__(self):
        self.head = None
    def swap(self,x,y):
        temp = self.head
        prev = None
        while(temp):
            if temp.data == x or temp.data == y:
                if temp.data == x:
                    swap_node_y = Node(y)
                    if temp == self.head:
                        self.head = swap_node_y
                        swap_node_y.next = temp.next
                    else:
                        prev.next = swap_node_y
                    swap_node_y.next = temp.next
                if temp.data == y:
                    swap_node_x = Node(x)
                    if temp == self.head:
                        self.head = swap_node_x
                        swap_node_x.next = temp.next
                    else:
                        prev.next = swap_node_x
                    prev.next = swap_node_x
                    swap_node_x.next = temp.next
            prev = temp
            temp = temp.next
    def print_LL(self):
        temp = self.head
        while(temp):
            print(temp.data,end=" ")
            temp = temp.next

if __name__=='__main__':
    llist = LL()
    llist.head = Node(10)
    second = Node(15)
    third = Node(12)
    four = Node(13)
    five = Node(20)
    six = Node(14)
    llist.head.next = second
    second.next = third
    third.next = four
    four.next = five
    five.next = six
    six.next = None
    llist.swap(15,13)
    llist.print_LL()


