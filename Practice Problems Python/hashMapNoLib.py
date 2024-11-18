class myNode:
    def __init__(self, key, value):
        self.next = None
        self.key = key
        self.value = value

class MyHashMap:

    def __init__(self):
        self.myHash = [None]*1000

    def put(self, key: int, value: int) -> None:
        index = key%1000
        currNode = self.myHash[index]
        if currNode == None:
            self.myHash[index] = myNode(key, value)  
            return
        while True:
            if currNode.key == key:
                currNode.value = value
                return
            if currNode.next == None:
                currNode.next = myNode(key, value)  
                return
            currNode = currNode.next
                
            
                      

    def get(self, key: int) -> int:
        index = key % 1000
        currNode = self.myHash[index]
        while True:
            if currNode == None:
                return -1
            if currNode.key == key:
                return currNode.value
            else:
                currNode = currNode.next

    def remove(self, key: int) -> None:
        index = key%1000
        prevNode = self.myHash[index]
        if prevNode == None:
            return
        currNode = prevNode.next
        if prevNode.key == key:
            self.myHash[index] = currNode
            return
        while True:
            if currNode == None:
                return
            if currNode.key == key:
                prevNode.next = currNode.next
                return
            else:
                prevNode = currNode
                currNode = currNode.next


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)