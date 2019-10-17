''' List Implementation '''

myStack = [] 
myStack.append(1)
myStack.append(2)
myStack.append(3)

# print(myStack.pop())
# print(myStack)

''' collections.deque Implementation '''

from collections import deque

myStack2 = deque()
myStack2.append(1)
myStack2.append(2)
myStack2.append(3)

# print(myStack2.pop())
# print(myStack2)


''' Using a doubley Linked List '''

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None 

class Stack: #contains Node Object 
    def __init__(self):
        self.head = None
    
    def push(self, value):
        if self.head == None:
            self.head = Node(value)
        else:
            newNode = Node(value)
            self.head.prev = newNode
            newNode.next = self.head
            newNode.prev = None
            self.head = newNode  
if __name__ == '__main__':
    stack = Stack()
    stack.head = Node(1)
    stack.push(2)
    stack.push(3)
    print(stack.head.value)