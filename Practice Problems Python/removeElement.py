class Solution(object):
    def removeElement(self, nums, val):
        count = 0
        while count < len(nums):
            if val == nums[count]:
                nums.remove(val)
            else:
                count += 1
            
        '''
        for i in range(count):
            nums.append(val)
        '''
        print(nums)
        return len(nums)
myObject = Solution()
nums = [3,2,2,3]
val = 3
k = myObject.removeElement(nums, val)
print(k)