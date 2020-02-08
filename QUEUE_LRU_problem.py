class Node:
	def __init__(self,data):
		self.data = data
		self.next = None
		self.prev = None
class lru:
	def __init__(self,size):
		self.front = None
		self.rear = None
		self.size = size
	def findlen(self):
		temp = self.front
		l = 0
		while(temp):
			temp = temp.next
			l = l + 1
		return l
	def enqueue(self,data):
		new_node = Node(data)
		l = self.findlen()
		temp = self.front
		if l == 0:
			self.front = self.rear = new_node
		elif l == self.size:
			self.front = self.front.next
			self.front.prev = None
			self.rear.next = new_node
			new_node.prev = self.rear
			self.rear = new_node
		else:
			while(l):
				if new_node.data == self.front.data:
					self.front = self.front.next
					self.front.prev = None
					self.rear.next = new_node
					new_node.prev = self.rear
					self.rear = new_node
					break
				if new_node.data == self.rear.data:
					break
				if new_node.data == temp.data:
					prev = temp.prev
					temp.prev.next = temp.next
					temp.next.prev = prev
					self.rear.next = new_node
					new_node.prev = self.rear
					self.rear = new_node
					temp = temp.next
					continue
				temp = temp.next
				l = l - 1
			else:
				self.rear.next = new_node
				new_node.prev = self.rear
				self.rear = new_node
	def print_list(self):
		temp = self.front
		while(temp):
			print(temp.data,end=" ")
			temp = temp.next

q = lru(4)
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(1)
q.enqueue(4)
q.enqueue(5)
q.print_list()

