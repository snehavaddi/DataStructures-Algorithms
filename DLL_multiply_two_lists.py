class Node:
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None
class DLL:
    def __init__(self):
        self.head = None
        self.last = None
    def print_list(self):
        temp = self.head
        while(temp):
            print(temp.data,end=" ")
            temp = temp.next
        print("\r")
    def list_append(self,data):
        if self.head == None:
            self.head = self.last = Node(data)
        else:
            new_node = Node(data)
            self.last.next = new_node
            new_node.prev = self.last
            self.last = new_node
    def find_product(self,list1,list2):
        temp1 = list1.last
        temp2 = list2.last
        c = 0
        q = 0
        sum = 0
        final = 0
        while(temp1):
            temp2 = list2.last
            while(temp2):
                p = int(temp1.data) * int(temp2.data)
                sum = sum + (p * pow(10,c))
                c = c + 1
                temp2 = temp2.prev
            sum = sum * (pow(10,q))
            final = final + sum
            sum = 0
            c = 0
            q = q + 1
            temp1 = temp1.prev
        final = str(final)
        self.head = None
        for i in final:
            self.list_append(i)
        self.print_list()


dlist1 = DLL()
dlist2 = DLL()
m = 55
n = 349
m = str(m)
n = str(n)
for i in m:
    dlist1.list_append(i)
dlist1.print_list()
for j in n:
    dlist2.list_append(j)
dlist2.print_list()
dlist1.find_product(dlist1,dlist2)

