class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class LL:
    def __init__(self):
        self.head = None
    def append(self,new_node_data):
        temp = self.head
        new_node = Node(new_node_data)
        while(temp):
            if(temp.next == None):
                temp.next = new_node
                new_node.next = None
            temp = temp.next
    def find_count(self,key):
        temp = self.head
        count = 0
        while(temp):
            if(temp.data == key):
                count = count + 1
            temp = temp.next
        print("number of times %d occurred in list is:" %key ,count)
    def find_loop(self):
        count = 0
        temp1 = self.head
        temp2 = self.head
        while(temp1):
            if(temp1 == None or temp2 == None or temp1.next == None or temp2.next == None or temp2.next.next == None):
                print("No Loop exits")
                break
            temp1 = temp1.next
            temp2 = temp2.next.next
            if(temp1 ==  temp2):
                self.head = temp1
                while(temp1):
                    count = count + 1
                    temp1 = temp1.next
                    if (temp1 == self.head):
                        return count
    def form_list(self):
        temp = self.head
        list1 = []
        while(temp):
            list1.append(temp.data)
            print(temp.data,end =" ")
            temp = temp.next
        return list1

class stack:
    def __init__(self,new_data):
        self.head = None
        if new_data:
            for data in new_data:
                self.push(data)
    def push(self,new_data):
        temp = Node(new_data)
        temp.next = self.head
        self.head = temp
    def pop(self,list1):
        i = 0
        temp1 = self.head
        while(temp1):
            temp = self.head.data
            self.head = self.head.next
            if temp != list1[i]:
                print("Not a palindrome")
            i = i + 1
            temp1 = temp1.next
        return True

if __name__=='__main__':
    llist = LL()
    llist.head = Node(1)
    second = Node(2)
    third = Node(3)
    fourth = Node(2)
    five = Node(1)
    llist.head.next = second
    second.next = third
#    third.next = None
    third.next = fourth
    fourth.next = five
    five.next = None
    list1 = llist.form_list()
    stack_list = stack(list1)
    if(stack_list.pop(list1)):
        print("Palindrome")

#    llist.is_palindrome(llist)
#    llist.append(2)
#    llist.append(1)
#    llist.append(1)
#    llist.print_LL()
#    llist.find_count(1)
