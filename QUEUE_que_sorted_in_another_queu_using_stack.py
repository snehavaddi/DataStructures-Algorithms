class Node:
	def __init__(self,data):
		self.data = data
		self.next = None
		self.prev = None
class sortqueue:
	def __init__(self):
		self.rear1 = None
		self.front1 = None
		self.rear2 = None
		self.front2 = None
		self.stack_head = None
	def push(self,data):
		new_node = Node(data)
		if self.rear1 == None:
			self.rear1 = self.front1 = new_node
		else:
			new_node.next = self.rear1
			self.rear1.prev = new_node
			self.rear1 = new_node
	def stack_push(self,temp):
		new_node = Node(temp.data)
		if self.stack_head == None:
			self.stack_head = new_node
		else:
			t = self.stack_head
			while(t):
				if temp.data > self.stack_head.data:
					self.stack_head.next = new_node
				t = t.next
			else:
				if self.rear2 == None:
					self.rear2 = self.front2 = new_node
				else:
					new_node.next = self.rear2
					self.rear2.prev = new_node
					self.rear2 = new_node

	def sortqueue(self):
		temp = self.front1
		while(temp):
			self.stack_push(temp)
			temp = temp.prev
		stack_ele = self.stack_head
		new_node = Node(stack_ele.data)
		while(stack_ele):
			new_node.next = self.rear2
			self.rear2.prev = new_node
			self.rear2 = new_node
			stack_ele = stack_ele.next
	def print_list(self):
		temp = self.rear2
		while(temp):
			print(temp.data,end=" ")
			temp = temp.next

q = sortqueue()
q.push(5)
q.push(1)
q.push(2)
q.push(3)
q.push(4)
q.print_list()
q.sortqueue()
q.print_list()
