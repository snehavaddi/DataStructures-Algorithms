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
    def print_LL(self):
        temp = self.head
        while(temp):
            print(temp.data,end =" ")
            temp = temp.next

if __name__=='__main__':
    llist = LL()
    llist.head = Node(1)
    second = Node(2)
    third = Node(3)
    fourth = Node(4)
    llist.head.next = second
    second.next = third
    fourth.next = second
    llist.append(2)
    llist.append(1)
    llist.append(1)
    llist.print_LL()
    llist.find_count(1)
