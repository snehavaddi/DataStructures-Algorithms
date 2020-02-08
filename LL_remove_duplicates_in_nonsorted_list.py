class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LL:
    def __init__(self):
        self.head = None
    def remove_dup(self):
        count = 0
        s = set()
        temp = self.head
        while(temp):
            if temp.data in s:
                prev.next = temp.next
                temp = temp.next
                continue
            s.add(temp.data)
            prev = temp
            temp = temp.next

    def print_LL(self):
        temp = self.head
        while(temp):
            print(temp.data,end=" ")
            temp = temp.next

if __name__=='__main__':
    llist = LL()
    llist.head = Node(1)
    second = Node(1)
    third = Node(1)
    four = Node(4)
    five = Node(1)
    llist.head.next = second
    second.next = third
    third.next = four
    four.next = five
    five.next = None
    llist.remove_dup()
    llist.print_LL()


