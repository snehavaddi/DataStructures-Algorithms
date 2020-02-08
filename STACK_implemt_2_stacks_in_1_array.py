class stack:
    def __init__(self,n):
        self.size = n
        self.arr = [None] * n
        self.top1 = -1
        self.top2 = self.size
    def push1(self,data):
        if self.top1 < self.top2:
            self.top1 = self.top1 + 1
            self.arr[self.top1] = data
    def push2(self,data):
        if self.top1 < self.top2:
            self.top2 = self.top2 - 1
            self.arr[self.top2] = data
    def pop1(self):
        if self.top1 >= 0:
            x = self.arr[self.top1]
            self.top1 = self.top1 - 1
            return x
    def pop2(self):
        if self.top2 <= self.size:
            x = self.arr[self.top2]
            self.top2 = self.top2 + 1
        return x

s = stack(5)
s.push1(10)
s.push2(10)
s.push1(20)
s.push2(20)
s.push1(30)

print(s.pop1())
print(s.pop1())
print(s.pop1())
print(s.pop2())
print(s.pop2())