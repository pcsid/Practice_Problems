class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        for char in s:
            if len(stack) == 0:
                stack.append(char)
            elif char == ")" and stack[-1] == "(":
                stack.pop()
            else:
                stack.append(char)
        return len(stack)
            