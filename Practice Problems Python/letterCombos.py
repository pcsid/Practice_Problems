class Solution(object):
    def letterCombinations(self, digits):
        myDict = {
            2: "a,b,c",
            3: "d,e,f",
            4: "g,h,i",
            5: "j,k,l",
            6: "m,n,o",
            7: "p,q,r,s",
            8: "t,u,v",
            9: "w,x,y,z"
        }
        myArr = ""
        for num in digits:
            num = int(num)
            if num < 9:
                myArr

            

myObject = Solution()
digits = "23"
myObject.letterCombinations(digits)