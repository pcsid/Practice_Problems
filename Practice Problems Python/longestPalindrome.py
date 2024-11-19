class Solution:
    def longestPalindrome(self, s: str) -> str:
        self.maxCount = 1
        self.maxStart = 0
        self.maxEnd = 0
        def expand(start, end):
            if start == end:
                count = -1
            else:
                count = 0
            while start >= 0 and end < len(s):
                if s[start] == s[end]:
                    count += 2
                    start -= 1
                    end += 1
                else:
                    break
            if count > self.maxCount:
                    self.maxCount = count
                    self.maxStart = start + 1
                    self.maxEnd = end - 1
        index = 0
        for char in s[:len(s)-1]:
            expand(index, index)
            expand(index, index+1)
            index += 1
        return s[self.maxStart:self.maxEnd+1]
