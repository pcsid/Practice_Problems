class Solution:
    def isValid(self, s: str) -> bool:
        myStack = []
        for char in s:
            if len(myStack) == 0:
                myStack.append(char)
            elif char == ")" and myStack[-1] == "(":
                myStack.pop()
            elif char == "]" and myStack[-1] == "[":
                myStack.pop()
            elif char == "}" and myStack[-1] == "{":
                myStack.pop()
            else:
                myStack.append(char)
        if len(myStack) == 0:
            return True
        return False