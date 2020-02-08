class Node:
	def __init__(self,data,prio):
		self.data = data
		self.prio = prio
		self.next = None
		self.prev = None
class pqueue:
	def __init__(self):
		self.head = None
	def push(self,data,prio):
		new_node = Node(data,prio)
		if self.head == None:
			self.head = new_node
		else:
			temp = self.head
			while(new_node.prio > temp.prio and temp.next != None):
				temp = temp.next
			else:
				if temp.next == None:
					temp.next = new_node
					new_node.prev = temp
				else:
					new_node.next = temp
					temp.prev = new_node
					self.head = new_node
	def pop(self):
		self.head = self.head.next
		self.head.prev = None

	def print_list(self):
		temp = self.head
		while(temp):
			print(temp.data,end=" ")
			temp = temp.next


pq = pqueue()
pq.push(4,1)
pq.push(5,2)
pq.push(6,3)
pq.push(7,0)
pq.pop()
pq.print_list()

