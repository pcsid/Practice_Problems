# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def averageOfLevels(self, root):
        avLevel = []
        queue = []
        queue.append(root)
        while (len(queue) != 0):
            nextQueue = []
            sumLevel = 0.0
            count = 0.0
            for node in queue:
                count += 1
                sumLevel += node.val
                if node.left != None:
                    nextQueue.append(node.left)
                if node.right != None:
                    nextQueue.append(node.right)
            avLevel.append(sumLevel/count)
            queue = nextQueue
        return avLevel
