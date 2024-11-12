# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#Use tortiouse and hare - two pointers - next time

class Solution(object):
    def hasCycle(self, head):
        myArr = []
        myNode = head
        while(myNode.value not in myArr):
            myArr.append(myNode.value)
            myNode = myNode.next
            if myNode.next == None:
                return False
        return True
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None