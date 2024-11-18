# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        currNode = head
        total = 0
        while currNode:
            total = total*2 + currNode.val
            currNode = currNode.next
        return total