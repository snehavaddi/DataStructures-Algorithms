class queue:
    def __init__(self):
        self.s1 = []
        self.s2 = []
    def push(self,data):
        self.s1.append(data)
    def enqueue(self,data):
        self.push(data)
    def dequeue(self):
        while(len(self.s1) != 0):
            x = self.s1.pop()
            self.s2.append(x)
        x = self.s2.pop()
        return x
q = queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
