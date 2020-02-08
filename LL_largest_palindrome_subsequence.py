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
    def len_palindrome(self):
        temp = self.head
        arr = []
        while(temp):
            arr.append(temp.data)
            temp = temp.next
        n = len(arr)
        count = 0
        i = 0
        temp = self.head
        while(n):
            if arr.pop() == temp.data:
                temp = temp.next
                count = count + 1
                n = n - 1
            else:
                count = 0
                n = n - 1
        return count



llist1 = LL()
llist2 = LL()
llist3 = LL()
llist4 = LL()
llist1.push(24)
llist1.push(12)
llist1.push(2)
llist1.push(3)
llist1.push(7)
llist1.push(3)
llist1.push(2)
l = llist1.len_palindrome()
print(l)
#llist1.print_list(l2)




