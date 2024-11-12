value = 0
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
class LinkedList:
    def __init__(self, value):
        starterNode = Node(value)
        self.head = starterNode
        self.tail = starterNode
    def addNode(self, value):
        addedNode = Node(value)
        self.tail.next = addedNode
        self.tail = self.tail.next
    def reverseList(self):
        prevNode = None
        currNode = self.head
        self.tail = self.head
        while currNode is not None:
            nextNode = currNode.next
            self.printList()
            currNode.next = prevNode
            if currNode is not self.head:
                print(f"flipping {currNode.value}.next to {prevNode.value}")
            #self.printList()
            prevNode = currNode
            currNode = nextNode
        self.head = prevNode
    def printList(self):
        current = self.head
        while current:
            print(current.value, end=" -> " if current.next else "\n")
            current = current.next

def main():
    # Create a linked list with the initial value 1
    linked_list = LinkedList(1)
    
    # Add values 2, 3, 4, 5, and 6 to the linked list
    for value in range(2, 7):
        linked_list.addNode(value)
    
    # Print the linked list to verify
    current = linked_list.head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next
    linked_list.reverseList()
    linked_list.printList()

# Call the main function
if __name__ == "__main__":
    main()