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

    def delete_pos(self,pos):
        temp = self.head
        count = 0
        while(temp):
            if count == pos:
                prev.next = temp.next
            prev = temp
            temp = temp.next
            count = count + 1

    def delete_ll(self):
        temp = self.head
        while(temp):
            self.head = temp.next
            temp = temp.next

    def search(self,ll,search_element):
        if not ll:
            return False
        if ll.data == search_element:
            return True
        return self.search(ll.next,search_element)

    def search_at_pos(self,list,pos):
        count = -1
        llist.search_node(list,pos,count)

    def search_node(self,list,pos,count):
        count = count + 1
        if count == pos:
            print(list.data)
            return (list.data)
        llist.search_node(list.next,pos,count)

    def nth_node(self,list,n):
        list_len = llist.ll_len(list)
        pos = list_len - n
        temp = list
        count = 0
        while(temp):
            if count == pos:
                print("Element at %d position from end is:" % n , temp.data)
            count = count + 1
            temp = temp.next

    def ll_len(self,list):
        count = 0
        temp = list
        while(temp):
            temp = temp.next
            count = count + 1
        return count

    def find_mid(self):
        ll_len = llist.ll_len(self.head)
        count = 0
        mid = int(ll_len/2)
        temp = self.head
        while(temp):
            if count == mid:
                print("middle element in list is:",temp.data)
            temp = temp.next
            count = count + 1


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
    llist.find_mid()
 #   if(llist.search(llist.head,6)):
 #       print("TRUE")
 #   else:
 #       print("False")
 #   llist.nth_node(llist.head,3)
  #  llist.search_at_pos(llist.head,2)
  #  llist.delete_ll()       #function to delete LL
 #   llist.delete_pos(1)
#    llist.delete_head()
 #   llist.delete_mid(4)
  #  llist.delete_end()
    llist.print()
