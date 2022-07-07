class Node:
    def __init__(self,value, next=None):
        self.value = value
        self.next = next
        
class LinkedList:
    def __init__(self):
        self.head = None
    
    def to_list(self):
        listing = []
        node = self.head
        while node:
            listing.append(node.value)
            node = node.next
        return listing
        
    
head = Node(2)
head.next = Node(4)
head.next.next = Node(5)
head.next.next.next = Node(7)
head.next.next.next.next = Node(10)
head.next.next.next.next.next = Node(1)
print(head.value)
print(head.next.value)

head.printList()
    