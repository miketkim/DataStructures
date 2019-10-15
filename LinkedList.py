class Node:
    def __init__(self, value):
        self.value = value 
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None


if __name__ == '__main__':
    llist = SinglyLinkedList()
    llist.head = Node(1)
    second = Node(2)
    third = Node(3)
    print(llist.head.value)
    print(llist.head.next == None)