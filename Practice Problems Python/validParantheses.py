class Solution(object):
    def isValid(self, s):
        myStack = Stack()
        for i in s:   
            shouldBeOpen = ""
            if i == ")":
                shouldBeOpen = myStack.pop()
                if not shouldBeOpen == "(":
                    return False
            elif i == "}":
                shouldBeOpen = myStack.pop()
                if not shouldBeOpen == "{":
                    return False
            elif i == "]":
                shouldBeOpen = myStack.pop()
                if not shouldBeOpen == "[":
                    return False
            else:
                myStack.push(i)
        if(myStack.isEmpty()):
            return True
        return False
class Stack:
    def __init__(self):
        self.items = []
    def push(self, num):
        self.items.append(num)
    def isEmpty(self):
        if len(self.items) == 0:
            return True
        return False
    def pop(self):
        if len(self.items) == 0:
            return None
        return self.items.pop()

myObject = Solution()
s = "]"
print(myObject.isValid(s))