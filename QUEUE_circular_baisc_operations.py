class cq:
	def __init__(self,capacity):
		self.front=0
		self.rear = 0
		self.q = [None]*capacity
		self.capacity = capacity
	def isFull(self):
		if(self.rear == self.front - 1):
			return True
		elif(self.rear == self.capacity and self.front == 0):
			return True
		else:
			return False
	def enqueue(self,data):
		if(self.isFull()):
			print("Queue is Full")
			return
		else:
			if self.rear == self.capacity and self.front != 0 :
				self.q[self.front-1] = data
				self.front = self.front - 1
			else:
				self.q[self.rear] = data
				self.rear = self.rear+1
	def isEmpty(self):
		if (self.front == self.rear == 0) and (self.q[self.front] is None):
			return True
		else:
			return False
	def dequeue(self):
		if(self.isEmpty()):
			print("Queue is empty")
			return
		else:
			print("popped element is:",self.q[self.front],end=" ")
			self.q[self.front] = None
			self.front = self.front + 1
	def print_list(self):
		temp = self.front
		while(self.rear != temp):
			if(temp == self.capacity):
				temp = 0
				print(self.q[temp], end=" ")
				continue
			print(self.q[temp],end=" ")
			temp = temp + 1
q1 = cq(4)
q1.enqueue(1)
q1.enqueue(2)
q1.enqueue(3)
q1.enqueue(4)
q1.print_list()
#q1.enqueue(5)
q1.dequeue()
q1.print_list()
q1.enqueue(9)
q1.print_list()
q1.enqueue(10)