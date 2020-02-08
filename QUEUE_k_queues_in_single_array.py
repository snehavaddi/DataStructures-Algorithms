class kqueue:
	def __init__(self,k,n):
		self.k = k
		self.n = n
		self.free = 0
		self.next = [i+1 for i in range(self.n)]
		self.next[n-1] = -1
		self.front = [-1]*self.k
		self.rear = [-1] * self.k
		self.arr = [0]*self.n
		self.top = 0
	def isFull(self):
		if self.free == -1:
			return  True
		else:
			return False
	def isEmpty(self,sn):
		if self.front[sn] == -1:
			return True
		else:
			return False
	def push(self,item,sn):
		if self.isFull():
			print("queue overflow")
		else:
			next_free = self.next[self.free]
			if (self.isEmpty(sn)):
				self.rear[sn]=self.front[sn] = self.free
			else:
				self.next[self.rear[sn]] = self.free
				self.rear[sn] = self.free
			self.next[self.free] = -1
			self.arr[self.free] = item
			self.free = next_free

	def pop(self,sn):
		if self.isEmpty(sn):
			print("Queue is empty")
		else:
			front_index = self.front[sn]
			self.front[sn] = self.next[front_index]
			self.next[front_index] = self.free
			self.free = front_index
			return self.arr[front_index]

k = kqueue(3,10)

k.push(15,2)
k.push(45,2)

k.push(17,1)
k.push(49,1)
k.push(39,1)

k.push(11,0)
k.push(9,0)
k.push(7,0)

print("popped element is:" , k.pop(2))
print("popped element is:" , k.pop(1))
print("popped element is:" , k.pop(1))
print("popped element is:" , k.pop(0))