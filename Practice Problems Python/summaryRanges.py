class Solution(object):
    def summaryRanges(self, nums):
        '''
        numDict = {}
        counter = 0
        for num in nums:
            if (num - 1) not in nums:
                numDict[counter] = [num]
            else:
                numDict[counter].append(num)
        '''
        #python 2
        myList = []
        if len(nums) == 0:
            #print("empty")
            return myList
        start = nums[0]
        #end = num
        end = nums[0]
        
        for num in nums:
            if num - 1 not in nums and num != nums[0]:
                if start != end:
                    myString = str(start) + "->"+ str(end)
                    myList.append(myString)
                else:
                    myList.append(str(start))
                start = num
                end = num
            else:
                end = num
            if num == nums[-1]:
                if start != end:
                    myString = str(start) + "->"+ str(end)
                    myList.append(myString)
                else:
                    myList.append(str(start))
        return(myList)
myObject = Solution()
nums = [0, 1, 2, 4, 5, 7]
nums = []
print(myObject.summaryRanges(nums))