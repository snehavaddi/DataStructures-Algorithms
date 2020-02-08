class queue:
    def __init__(self):
        self.s1 = []
        self.min = []
    def enqueue(self,data):
        if len(self.s1) == 0:
            self.s1.append(data)
            self.min.append(data)
        else:
            self.s1.append(data)
            x = self.min.pop()
            self.min.append(x)
            if x < data:
                self.min.append(x)
            else:
                self.min.append(data)
    def dequeue(self):
        return self.s1.pop()
    def get_min(self):
        x = self.min.pop()
        # self.min.append(x)
        return x
q = queue()
q.enqueue(2)
q.enqueue(3)
q.enqueue(1)
print(q.get_min())
print(q.dequeue())
print(q.get_min())
