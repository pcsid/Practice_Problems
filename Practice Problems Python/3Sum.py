class Solution(object):
    def threeSum(self, nums):
        returnList = []
        nums.sort()

        startIndex = 0
        for i in nums:
            if startIndex == len(nums) - 2:
                break
            pointOne = startIndex + 1
            pointTwo = len(nums) - 1
            while pointTwo > pointOne:
                if nums[startIndex] + nums[pointOne] + nums[pointTwo] == 0:
                    if([nums[startIndex], nums[pointOne], nums[pointTwo]] not in returnList):
                        returnList.append([nums[startIndex], nums[pointOne], nums[pointTwo]])
                    pointTwo -= 1
                elif nums[startIndex] + nums[pointOne] + nums[pointTwo] > 0:
                    pointTwo -= 1
                elif nums[startIndex] + nums[pointOne] + nums[pointTwo] < 0:
                    pointOne += 1

            startIndex += 1
        
        return returnList
        