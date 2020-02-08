class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class DLL:
    def __init__(self):
        self.head = None

    def printlist(self):
        temp = self.head
        while (temp):
            print(temp.data, end=" ")
            temp = temp.next

    def find_len(self):
        temp = self.head
        length = 0
        while (temp):
            temp = temp.next
            length = length + 1
        return length

    def reverse_k(self,head,k):
        current = head
        next = None
        prev = None
        count = 0
        while (current is not None and count < k):
            next = current.next
            current.next = prev
            current.prev = next
            prev = current
            current = next
            count += 1
        if next is not None:
            head.next = self.reverse_k(next, k)
        return prev

dllist = DLL()
dllist.head = Node(1)
second = Node(2)
third = Node(3)
fourth = Node(4)
five = Node(5)
six = Node(6)
seven = Node(7)
dllist.head.next = second
second.next = third
second.prev = dllist.head
third.next = fourth
third.prev = second
fourth.next = five
fourth.prev = third
five.next = six
five.prev = fourth
six.next = seven
six.prev = five
seven.prev = six
#print("original list is:")
#dllist.printlist()
l = dllist.find_len()
k = 3
dllist.head = dllist.reverse_k(dllist.head,k)
dllist.printlist()


