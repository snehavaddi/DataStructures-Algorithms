class Node:
	def __init__(self,data):
		self.data = data
		self.next = None
		self.prev = None

class ll:
	def __init__(self):
		self.front = None
		self.rear = None
	def push(self,data):
		new_node = Node(data)
		if self.front == None:
			self.front = self.rear = new_node
		else:
			self.rear.prev = new_node
			new_node.next = self.rear
			self.rear = new_node
	def pop(self):
		print("popped element is",self.front.data,end=", ")
		self.front = self.front.prev
		self.front.prev.next = None
	def print_list(self):
		temp = self.front
		while(temp):
			print(temp.data,end=" ")
			temp = temp.prev

l = ll()
l.push(1)
l.push(2)
l.push(3)
l.push(4)
l.print_list()
l.pop()
l.print_list()




