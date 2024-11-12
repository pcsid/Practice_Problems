class Solution:
    def subsets(self, nums):
        res = []
        subset = []
        def dfs(i):
            if i == len(nums):
                res.append(subset.copy())
                return
            
            #add i value
            subset.append(nums[i])
            dfs(i + 1)

            #dont add i value
            subset.pop()
            dfs(i + 1)
        
        dfs(0)
        return res