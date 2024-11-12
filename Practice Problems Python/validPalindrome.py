
class Solution(object):
    def isPalindrome(self, s):
        isPalindrome = True
        i = 0
        j = len(s) - 1
        while i < j and isPalindrome:  

            while not s[i].isalpha() and not s[i].isnumeric():
                i += 1
                if(i == len(s)):
                    break
            while not s[j].isalpha() and not s[j].isnumeric():
                j -= 1
                if(j == -1):
                    break
            if j<= i: 
                return True
            if s[i].lower() == s[j].lower():
                i += 1
                j -= 1
            else :
                isPalindrome = False
        return isPalindrome

s = "A man, a plan, a canal: Panama"
myObject = Solution()

k = myObject.isPalindrome("0P")
print(k)
print("0".isnumeric())