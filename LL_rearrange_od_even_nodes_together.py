class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LL:
    def __init__(self):
        self.head = None
    def push(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data,end=" ")
            temp = temp.next
    def arrange_list(self):
        if self.head == None or self.head.next == None:
            return
        other = []
        count = 0
        prev = None
        temp = self.head
        while(temp):
            if temp.next == None and temp.data % 2 == 0 and temp != self.head and count == 2:
                other.append(temp.data)
                prev.next = None
                i = 0
                l = len(other)
                while(i< l):
                    new_node = Node(other[i])
                    prev.next = new_node
                    prev = new_node
                    i = i + 1
                break
            if temp.next == None and temp.data % 2 != 0 and temp != self.head and count == 1:
                other.append(temp.data)
                prev.next = None
                i = 0
                l = len(other)
                while (i < l):
                    new_node = Node(other[i])
                    prev.next = new_node
                    prev = new_node
                    i = i + 1
                break
            if temp.next == None and temp.data % 2 == 0 and temp != self.head and count == 1:
                other.append(temp.data)
                prev.next = None
                i = 0
                l = len(other)
                while(i< l):
                    new_node = Node(other[i])
                    prev.next = new_node
                    prev = new_node
                    i = i + 1
                break
            if temp.next == None and temp.data % 2 != 0 and temp != self.head and count == 2:
                other.append(temp.data)
                prev.next = None
                i = 0
                l = len(other)
                while (i < l):
                    new_node = Node(other[i])
                    prev.next = new_node
                    prev = new_node
                    i = i + 1
                break
            if  temp.data % 2 == 0  and temp == self.head:
                count = 1
            if temp.data % 2 != 0 and temp == self.head:
                count = 2
#            if temp.data % 2 == 0 and temp != self.head and count == 1:
#                continue
#            if temp.data % 2 != 0 and temp != self.head and count == 2:
#                continue
            if temp.data % 2 == 0 and temp != self.head and count == 2:
                prev.next = temp.next
                other.append(temp.data)
            if temp.data % 2 != 0 and temp != self.head and count == 1:
                prev.next = temp.next
                other.append(temp.data)
            prev = temp
            temp = temp.next



llist = LL()
llist.push(70)
llist.push(56)
llist.push(43)
llist.push(30)
llist.push(22)
llist.push(10)
llist.arrange_list()

llist.printList()

