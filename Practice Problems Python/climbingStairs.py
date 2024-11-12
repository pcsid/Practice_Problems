class recursiveSolution(object):
    def climbStairs(self, n):
        if n == 1 or n == 0: 
            return 1
        return self.climbStairs(n-2) + self.climbStairs(n-1)
class Solution(object):
    def climbStairs(self, n):
        dp = []
        for i in range(n + 1):
            if i == 1 or i == 0: 
                dp.append(1)
            else:
                dp.append(dp[i-2] + dp[i-1])
        return dp[n]
    
myObject = recursiveSolution()
mySecondObject = Solution()
print(mySecondObject.climbStairs(5))
print(myObject.climbStairs(5))