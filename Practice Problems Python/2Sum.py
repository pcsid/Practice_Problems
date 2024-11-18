class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:       
        myHash = {}

        for i, num in enumerate(nums):
            lookingFor = target - num
            if lookingFor in myHash:
                return i, myHash[lookingFor]
            myHash[num] = i