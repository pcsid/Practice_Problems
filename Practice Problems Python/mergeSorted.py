class Solution(object):
    def merge(self, nums1, m, nums2, n):
        if (m == 0):
            count = 0
            for num2 in nums2:
                nums1[count] = num2
                count += 1
            return
        topIndex = m - 1
        num1Counter = 0
        for num2 in nums2:
            merged = False
            while(not merged):
                if num2 < nums1[num1Counter]:
                    nums1 = self.move(nums1, topIndex, num1Counter, num2)
                    merged = True
                    n -= 1
                    topIndex += 1 
                    print(nums1)
                    
                elif nums1[topIndex] <= num2:
                    merged = True
                    topIndex += 1
                    num1Counter = topIndex
                    n -= 1
                    nums1[topIndex] = num2
                num1Counter += 1
                '''
                elif num1Counter > len(nums1) - n:
                    nums1[num1Counter] = num2
                    merged = True
                    n -= 1
                    topIndex += 1
                    print(nums1)
                '''
        print(nums1)
                
    
    def move(self, arr, topIndex, stopIndex, newNum):
        while topIndex >= stopIndex:
            arr[topIndex + 1] = arr[topIndex] 
            topIndex -= 1
        arr[topIndex + 1] = newNum
        return arr
    
nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [4,5,6]
n = 3

myObject = Solution()
myObject.merge(nums1, m, nums2, n)