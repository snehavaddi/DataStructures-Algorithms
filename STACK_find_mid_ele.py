class Node:
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None
class stack:
    def __init__(self):
        self.head = None
        self.mid = None
        self.count = 1
    def push(self,data):
        new_node = Node(data)
        if self.head != None:
            new_node.next = self.head
            self.head.prev = new_node
            if self.count%2 != 0:
                self.mid = self.mid.prev
            self.head = new_node
            self.count = self.count + 1
        else:
            new_node.next = self.head
            self.head = new_node
            self.mid = self.head
            self.count = self.count + 1
    def find_len(self):
        temp = self.head
        l = 0
        while(temp):
            temp = temp.next
            l = l + 1
        return l
    def find_mid(self):
        x = self.mid.data
        return x
    def pop(self):
        x = self.head.data
        self.head = self.head.next
        return x


s = stack()
s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.push(5)

l = s.find_len()
mid_ele = s.find_mid()
print(mid_ele)
print(s.pop())

