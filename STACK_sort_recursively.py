class stack:
	def __init__(self):
		self.stack = []
	def push(self,item):
		self.stack.append(item)
	def sort_if(self,item):
		if len(self.stack) == 0 or item < self.stack[-1]:
			self.push(item)
		else:
			temp = self.stack.pop()
			self.sort_if(item)
			self.stack.append(temp)
	def sort_arr(self):
		if len(self.stack) != 0:
			temp = self.stack.pop()
			self.sort_arr()
			self.sort_if(temp)
	def print(self):
		print("hello")
stack = stack()
stack.push(-3)
stack.push(14)
stack.push(18)
stack.push(-5)
stack.push(30)

stack.sort_arr()
stack.print()