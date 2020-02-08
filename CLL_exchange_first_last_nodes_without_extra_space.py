class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class CLL:
    def __init__(self):
        self.head = None
    def push(self,data):
        new_node = Node(data)
        new_node.next = self.head
        if self.head != None:
            temp = self.head
            while (temp.next != self.head):
                temp = temp.next
            temp.next = new_node
        else:
            new_node.next = new_node
        self.head = new_node
    def exchange_nodes(self):
        ptr1 = self.head
        ptr2 = self.head
        while(ptr2.next.next != self.head):
            ptr2 = ptr2.next
        next2 = ptr2.next
        next1 = ptr1.next
        ptr2.next = self.head
        self.head.next = next2
        self.head = next2
        self.head.next = next1
#other method in below commented lines:
 #       p.next.next = head.next;
 #       head.next = p.next;
 #       p.next = head;
 #       head = head.next;

    def print_list(self):
            temp = self.head
            if self.head != None:
                while(temp.next != self.head):
                    print(temp.data,end=" ")
                    temp = temp.next
                print(temp.data)
clist = CLL()
clist.push(4)
clist.push(3)
clist.push(2)
clist.push(1)
clist.push(5)
clist.exchange_nodes()
clist.print_list()
