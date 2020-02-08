class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class DLL:
    def __init__(self):
        self.head = None

    def printlist(self,list):
        temp = list
        while (temp):
            print(temp.data, end=" ")
            temp = temp.next

    def find_len(self,list):
        temp = list
        length = 0
        while (temp):
            temp = temp.next
            length = length + 1
        return length

    def reverse_k(self,head):
        current = head
        next = None
        prev = None
        count = 0
        while (current is not None):
            next = current.next
            current.next = prev
            current.prev = next
            prev = current
            current = next
        return prev

    def sort(self,list):
        curr = list.head
        if curr.data > curr.next.data:
            curr = dllist.reverse_k(curr)
            return curr
        while(curr.next):
            if curr.data > curr.next.data:
                curr.prev.next = None
                curr.prev = None
                curr = dllist.reverse_k(curr)
                l1 = dllist.find_len(dllist.head)
                l2 = dllist.find_len(curr)
                list = dllist.merge(dllist.head,curr,l1,l2)
                return list
            else:
                next = curr.next
                prev = curr
                curr = next
        return self.head

    def merge(self,list1,list2,l1,l2):
        if l1 > l2:
            list = list1
        else:
            list = list2
        while(list2):
            if list1.next == None or list2.next == None:
                if list1.next == None and list2.next != None:
                    new_node = Node(list2.data)
                    previous = list1.prev
                    list1.prev.next = new_node
                    new_node.next = list1
                    list1.prev = new_node
                    new_node.prev = previous
                    list1.next = list2.next
                    return head
                else:
                    list2.next = list1
                    break
            elif list1.data > list2.data:
                if list1 == dllist.head:
                    new_node = Node(list2.data)
                    new_node.next = list1
                    list1.prev = new_node
                    list1 = new_node
                    head = list1
                    list1 = list1.next.next
                    list2 = list2.next
                else:
                    new_node = Node(list2.data)
                    previous = list1.prev
                    list1.prev.next = new_node
                    new_node.next = list1
                    list1.prev = new_node
                    new_node.prev = previous
                    list1 = list1.next
                    list2 = list2.next
            elif list1.data < list2.data:
                list1 = list1.next
                list2 = list2.next


dllist = DLL()
dllist.head = Node(8)
second = Node(7)
third = Node(6)
fourth = Node(5)
five = Node(4)
six = Node(3)
seven = Node(2)
eight = Node(1)
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
seven.next = eight
eight.prev = seven
print("original list is:")
#dllist.printlist()
#l = dllist.find_len()
list = dllist.sort(dllist)
dllist.printlist(list)



