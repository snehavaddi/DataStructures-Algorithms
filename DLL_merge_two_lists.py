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
    def merge(self,list1,list2):
        if list1 == None:
            return list2
        if list2 == None:
            return list1
        if (list1 and list2):
            if list1.data < list2.data:
                sort_ptr = list1
                list1 = list1.next
            else:
                sort_ptr = list2
                list2 = list2.next
        new_head = sort_ptr
        while(list1 and list2):
            if list1.data < list2.data:
                sort_ptr.next = list1
                list1.prev = sort_ptr
                sort_ptr = list1
                list1 = sort_ptr.next
            else:
                sort_ptr.next = list2
                list2.prev = sort_ptr
                sort_ptr = list2
                list2 = sort_ptr.next
        if list1 == None:
            sort_ptr.next = list2
        else:
            sort_ptr.next = list1
        temp = new_head
        print("\r")
        while(temp):
            print(temp.data,end=" ")
            temp = temp.next

dllist1 = DLL()
dllist2 = DLL()
dllist1.head = Node(1)
second = Node(4)
third = Node(6)
fourth = Node(10)
five = Node(12)
#six = Node(3)
#seven = Node(2)
#eight = Node(1)

dllist2.head = Node(2)
second2 = Node(5)
third2 = Node(7)

dllist1.head.next = second
second.next = third
second.prev = dllist1.head
third.next = fourth
third.prev = second
fourth.next = five
fourth.prev = third
five.next = None
five.prev = fourth

dllist2.head.next = second2
second2.next = third2
second2.prev = dllist2.head
third2.prev = second2
print("original list is:")
#dllist.printlist()
l1 = dllist1.find_len()
l2 = dllist1.find_len()
dllist1.printlist()
print("\r")
dllist2.printlist()
if l1 > l2:
    dllist1.merge(dllist1.head,dllist2.head)
else:
    dllist2.merge(dllist1.head,dllist2.head)




