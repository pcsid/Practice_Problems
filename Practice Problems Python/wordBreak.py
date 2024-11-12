class Solution(object):
    def wordBreak(self, s, wordDict):
        dp = [False] * (len(s) + 1)
        #no letter
        dp[0] = True
        for i in range(1, len(s)+1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break
        return dp[-1]

myObject = Solution()
s = "appleman"
wordDict = ["apple", "man"]
print(myObject.wordBreak(s, wordDict))