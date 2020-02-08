class XORLinkedListNode(object):

    def __init__(self, val, prev, next):
        self.val = val
        self.both = prev ^ next

    def next_node(self, prev_idx):
        return self.both ^ prev_idx

    def prev_node(self, next_idx):
        return self.both ^ next_idx


class XORLinkedList(object):

    def __init__(self):
        self.memory = [XORLinkedListNode(None, -1, -1)]

    def head(self):
        return 0, -1, self.memory[0]  # head node index, prev node index, head node

    def add(self, val):
        current_node_index, previous_node_index, current_node = self.head()
        while True:  # walk down the list until we find the end
            next_node_index = current_node.next_node(previous_node_index)
            if next_node_index == -1:  # we reached the end on the list
                break
            previous_node_index, current_node_index = current_node_index, next_node_index
            current_node = self.memory[next_node_index]

        new_node_index = len(self.memory)  # "allocation"
        current_node.both = previous_node_index ^ new_node_index
        self.memory.append(XORLinkedListNode(val, current_node_index, -1))

    def get(self, index):
        current_index, previous_index, current_node = self.head()
        for cnt in range(index + 1):
            previous_index, current_index = current_index, current_node.next_node(previous_index)
            current_node = self.memory[current_index]
        print(current_node.val)
    #    return current_node.val

#return XORLinkedList()
dlist = XORLinkedList()
dlist.add(1)
dlist.add(2)
dlist.add(3)
dlist.add(4)
dlist.add(5)
for i in  range(5):
    dlist.get(i)
