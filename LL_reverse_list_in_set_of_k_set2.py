class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def reverse(self, head, k):
        curr = self.head
        prev = None
        next = None
        count = 0
        new_stack = []
        while(curr is not None):
            count = 0
            while(curr is not None and count < k):
                new_stack.append(curr.data)
                curr = curr.next
                count = count + 1
            while(new_stack):
                if prev == None:
                    prev = Node(new_stack.pop())
                    self.head = prev
                else:
                    prev.next = Node(new_stack.pop())
                    prev = prev.next
        prev.next = None
        return self.head

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data,end=" ")
            temp = temp.next
llist = LinkedList()
llist.push(9)
llist.push(8)
llist.push(7)
llist.push(6)
llist.push(5)
llist.push(4)
llist.push(3)
llist.push(2)
llist.push(1)

print("Given linked list")
llist.printList()
llist.head = llist.reverse(llist.head, 3)

print("\nReversed Linked list")
llist.printList()