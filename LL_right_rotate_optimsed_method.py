# Python program to rotate a linked list

# Node class
class Node:

    # Constructor to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    # Function to initialize head
    def __init__(self):
        self.head = None

    # Function to insert a new node at the beginning
    def push(self, new_data):
        # allocate node and put the data
        new_node = Node(new_data)

        # Make next of new node as head
        new_node.next = self.head

        # move the head to point to the new Node
        self.head = new_node

    # Utility function to prit the linked LinkedList
    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data,end=" ")
            temp = temp.next

    def rotate(self, k):
        if k == 0:
            return
        current = self.head
        count = 1
        while (count < k and current is not None):
            current = current.next
            count += 1
        if current is None:
            return
        kthNode = current
        while (current.next is not None):
            current = current.next
        current.next = self.head
        self.head = kthNode.next
        kthNode.next = None

llist = LinkedList()
for i in range(60, 0, -10):
    llist.push(i)
print("Given linked list")
llist.printList()
llist.rotate(4)
print("\nRotated Linked list")
llist.printList()

# This code is contributed by Nikhil Kumar Singh(nickzuck_007)
