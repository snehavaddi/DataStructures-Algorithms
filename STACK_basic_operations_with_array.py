from sys import maxsize

def createStack():
    stack = []
    return stack
def isEmpty(stack):
    if len(stack) == 0:
        return 0
    else:
        return len(stack)
def push(stack,item):
    stack.append(item)
    print(item,"item pushed to stack")
def pop(stack):
    if(not isEmpty(stack)):
        return 0
    else:
        return stack.pop()
def display_stack():
    l = len(stack)
    i = 0
    while(l):
        print(stack[i])
        i = i+1
        l = l - 1

stack = createStack()
push(stack,str(10))
push(stack,str(20))
push(stack,str(30))
push(stack,str(40))
push(stack,str(50))
print(pop(stack),"item popped from stack")
display_stack()