class Solution(object):
    def searchInsert(self, nums, target):
        #binary search
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        #print(mid)
        if nums[mid] > target:
            return mid
        else:
            return mid + 1
myObject = Solution()
nums = [1,3,5,7]
target = 6
print(myObject.searchInsert(nums, target))