class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LL:
    def __init__(self):
        self.head = None
    def push(self,push_data):
        push_data_node = Node(push_data)
        push_data_node.next = self.head
        self.head = push_data_node
    def insert(self,prev_node_data,insert_data):
        temp = self.head
        while(temp):
            if temp.data == prev_node_data:
                insert_node = Node(insert_data)
                insert_node.next = temp.next
                temp.next = insert_node
            temp = temp.next

    def insert_end(self,insert_data):
        insert_node = Node(insert_data)
        temp = self.head
        while(temp):
            if temp.next == None:
                temp.next = insert_node
                insert_node.next = None
            temp = temp.next
    def delete_head(self):
        self.head = self.head.next

    def delete_mid(self,current_node_data):
        temp = self.head
        while(temp):
            if temp.data == current_node_data:
                prev.next = temp.next
            prev = temp
            temp = temp.next

    def delete_end(self):
        temp = self.head
        while(temp):
            if temp.next == None:
                prev.next = None
            prev = temp
            temp = temp.next

    def print(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next

if __name__=='__main__':
    llist = LL()
    llist.head = Node(1)
    second = Node(2)
    third = Node(3)
    llist.head.next = second
    second.next = third
    third.next = None
    llist.push(0)
    llist.insert(2,4)
    llist.insert_end(5)
    llist.delete_head()
    llist.delete_mid(4)
    llist.delete_end()
    llist.print()
