from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 1

        for j in range(1, len(nums)):
            if nums[j] != nums[i - 1]:
                nums[i] = nums[j]
                i += 1
        
        return i
    
print("Test case: [1,2,2]")
nums = [1,2,2]
solution = Solution()
result = solution.removeDuplicates(nums)
print("Expected output: [1,2]")
print("Actual output:", nums[:result])
print("Length of result:", result)