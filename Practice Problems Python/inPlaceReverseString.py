from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        left = 0
        right = len(s) - 1

        while left < right:
            leftValue = s[left]
            s[left] = s[right]
            s[right] = leftValue
            left += 1
            right -= 1
        