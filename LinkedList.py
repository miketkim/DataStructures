class Node:
    def __init__(self, value):
        self.value = value 
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
    
    def traverse(self):
        currentNode = self.head 
        while (currentNode):
            print(currentNode.value)
            currentNode = currentNode.next
    
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~  INSERT METHODS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    def prepend(self, value):
        # newNode = Node(value)
        # Time Complexity = O(1)
        value.next = self.head
        self.head = value 
    
    def append(self, value):
        # Time Complexity = O(n)
        newNode = Node(value)
        currentNode = self.head
        while (currentNode.next):
            currentNode = currentNode.next 
        currentNode.next = newNode

    def insertAfter(self, prevNode, value):
        # Time Complexity = O(1)
        if prevNode == None:
            print "${prevNode} not in linked list"
            return 
        newNode = Node(value)
        newNode.next = prevNode.next 
        prevNode.next = newNode
    
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ SEARCH METHODS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def find(self, value):
        currentNode = self.head
        while currentNode and currentNode.value != value:
            currentNode = currentNode.next 
        return currentNode
    

    


if __name__ == '__main__':
    llist = SinglyLinkedList()
    llist.head = Node(1)
    second = Node(2)
    third = Node(3)

    # llist.prepend(second)
    llist.head.next = second; 
    second.next = third; 
    ## llist.append(18001)
    print(llist.find(3).value)

    # llist.traverse()