# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        myList = [] 

        def traverse(root):
            if root != None:
                myList.append(root.val)
                return traverse(root.left), traverse(root.right)
            else: return

        traverse(root)
        myList.sort()

        low = 0
        high = len(myList) - 1

        while high > low:
            if myList[low] + myList[high] == k: