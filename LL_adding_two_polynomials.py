class Node:
    def __init__(self,data1,data2):
        self.data1 = data1
        self.data2 = data2
        self.next = None
class LL:
    def __init__(self):
        self.head = None
    def push(self,data1,data2):
        new_node = Node(data1,data2)
        new_node.next = self.head
        self.head = new_node
    def print_list(self,l):
        temp = l.head
        while(temp):
            print(temp.data1,"x^",temp.data2, end=' ')
            temp = temp.next
    def find_addition(self,l1,l2):
        count1 = self.find_len(l1)
        count2 = self.find_len(l2)
        if count1 >  count2:
            n = count1
        elif count1 < count2:
            n = count2
        else:
            n = count1
        temp1 = l1.head
        temp2 = l2.head
        while(n):
            if temp1.data2 > temp2.data2:
                temp1 = temp1.next
                n = n - 1
            elif temp1.data2 < temp2.data2:
                temp2 = temp2.next
                n = n - 1
            else:
                temp1.data1 = temp1.data1 + temp2.data1
                n = n - 1
                temp1 = temp1.next
                temp2 = temp2.next
        return l1

    def find_len(self,l):
        temp = self.head
        count = 0
        while(temp):
            temp = temp.next
            count = count + 1
        return count
llist1 = LL()
llist2 = LL()
llist1.push(2,0)
llist1.push(4,1)
llist1.push(5,2)
llist2.push(5,0)
llist2.push(5,1)
l = llist1.find_addition(llist1,llist2)
llist1.print_list(l)




