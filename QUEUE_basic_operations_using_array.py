class queue:
	def __init__(self):
		self.q = []
	def enqueue(self,data):
		self.q.append(data)
	def dequeue(self):
		self.q.pop(0)
	def que_front(self):
		l = len(self.q)
		print("front element is:" ,self.q[l-1])
	def que_end(self):
		print("end element is", self.q[0])
	def printlist(self):
		l = len(self.q)
		for i in range(l):
			print(self.q[i])

q1 = queue()
q1.enqueue(1)
q1.enqueue(2)
q1.enqueue(3)
q1.enqueue(4)
q1.enqueue(5)
q1.enqueue(6)
q1.dequeue()
q1.que_front()
q1.que_end()
q1.printlist()
