class Solution(object):
    def minimumTotal(self, triangle):
        #print(triangle[0])
        if len(triangle) == 1:
            return triangle[0][0]
        i = len(triangle) - 2

        while(i>=0):
            numCounter = 0
            for num in triangle[i]:
                triangle[i][numCounter] = num + (min(triangle[i+1][numCounter], triangle[i+1][numCounter + 1]))
                numCounter += 1
            i -= 1
        return triangle[0][0]

myObject = Solution()
triangle1 = [[2],[3,4],[6,5,7],[4,1,8,3]]
print(myObject.minimumTotal(triangle1))
