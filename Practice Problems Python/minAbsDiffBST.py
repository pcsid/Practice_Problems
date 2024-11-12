# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
            self.minDiff = float('inf')  # Instance variable
            self.checkedArr = []     
    
    def getMinimumDifference(self, root):
       
        #print(self.checkedArr)
        self.recursive(root)
        self.checkedArr.sort()
        count = 1
        while count < len(self.checkedArr):
            if self.checkedArr[count] != None and self.checkedArr[count - 1] != None:
                if abs(self.checkedArr[count] - self.checkedArr[count - 1]) < self.minDiff:
                    self.minDiff = abs(self.checkedArr[count] - self.checkedArr[count - 1])
            count += 1
        return self.minDiff
    def recursive(self, root):
        self.checkedArr.append(root.val)
        #print("total arr", self.checkedArr)
        #print("Added ", root.val)
        if root.left == None:
            if root.right == None:
                return None
            else:
                return self.recursive(root.right)
        else:
            if root.right == None:
                return self.recursive(root.left)
            else:
                return self.recursive(root.left), self.recursive(root.right) 
