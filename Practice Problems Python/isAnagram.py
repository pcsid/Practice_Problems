class Solution(object):
    def isAnagram(self, s, t):
        sDict = {}
        tDict = {}
        if len(s) != len(t):
            return False
        for c in range(len(s)):
            if s[c] in sDict:
                sDict[s[c]] += 1
            else:
                sDict[s[c]] = 1
            if t[c] in tDict:
                tDict[t[c]] += 1
            else:
                tDict[t[c]] = 1
        return(sDict == tDict)
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
myObject = Solution()
s = "anagram"
t = "nagaram"
print(myObject.isAnagram(s, t))

a = {"Hi":3, "Bye":2}
b = {"Hi":3, "Bye":3}
print(a==b)
