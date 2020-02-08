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
    def decimal_sum(self):
        sum = 0
        curr = self.head
        while(curr):
            sum = sum*2 + curr.data
            curr = curr.next
        print(sum)
    def print_list(self,l):
        temp = l.head
        while(temp):
            print(temp.data, end=' ')
            temp = temp.next
    def find_len(self,li):
        temp = li.head
        count = 0
        while(temp):
            count = count + 1
            temp = temp.next
        return count
    def append_zero(self,li,c1,c2):
        n = abs(c1-c2)
        temp = li.head
        while(n):
            new_node = Node(0)
            new_node.next = li.head
            li.head = new_node
            n = n-1
    def reverse(self,l):
        curr = l.head
        prev = None
        while(curr):
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        self.head = prev

    def sub(self,l1,l2):
        temp1 = l1.head
        temp2 = l2.head
        borrow = 0
        while(temp1):
            temp1.data = temp1.data - borrow
            if(temp1.data - temp2.data < 0):
                temp1.data = 10 + temp1.data
                temp1.data = temp1.data - temp2.data
                borrow = 1
            elif(temp1.data - temp2.data >= 0):
                temp1.data = temp1.data - temp2.data
            temp1 = temp1.next
            temp2 = temp2.next
    def rearrange(self,k,l1,l2,l3,l4):
        temp = l1.head
        while(temp):
            if temp.data < k :
                l2.push(temp.data)
                temp = temp.next
                continue
            if temp.data == k :
                l3.push(temp.data)
                temp = temp.next
                continue
            if temp.data > k:
                l4.push(temp.data)
                temp = temp.next
                continue
        count = l1.head
        temp2 = l2.head
        c = 1
        while(count):
            if temp2.next == None and c == 1:
                temp2.next = l3.head
                c = 2
            if temp2.next == None and c == 2:
                temp2.next = l4.head
                c = 3
            count = count.next
            temp2 = temp2.next
        return l2

llist1 = LL()
llist2 = LL()
llist3 = LL()
llist4 = LL()
llist1.push(3)
llist1.push(2)
llist1.push(5)
llist1.push(2)
llist1.push(3)
llist1.push(4)
llist1.push(1)
l2 = llist1.rearrange(3,llist1,llist2,llist3,llist4)
llist1.print_list(l2)




