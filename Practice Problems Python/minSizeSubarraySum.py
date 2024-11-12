class Solution(object):
    def minSubArrayLen(self, target, nums):
    
        if nums[-1] > target:
            return 1

        #build first subarray
        start = 0
        end = 0
        subSum = 0
        maxCount = 0
        tempCount = 0
        for num in nums:
            subSum += num
            tempCount += 1
            if subSum >= target:
                break
            end += 1
            #if whole array doesnt add up to target, return 0
        if subSum < target:
            return 0
        maxCount = tempCount

        while end != (len(nums)) and start != end:
            #this first block where shortening happens
            subSum -= nums[start]
            start += 1
            tempCount -= 1
            #if lower, start loop to move end till higher again
            while subSum < target and end != len(nums) - 1:
                tempCount += 1
                end += 1
                subSum += nums[end]
            #check if we got new shorterst
            if tempCount < maxCount and subSum >= target:
                maxCount = tempCount

        return maxCount
myObject = Solution()
target = 7
nums = [2,3,1,2,4,3]
print(myObject.minSubArrayLen(target, nums))