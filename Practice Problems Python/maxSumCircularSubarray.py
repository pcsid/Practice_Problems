class Node():
    def __init__(self, value):
        self.value = value
        self.next = None
        self.back = None

class Solution(object):
    def maxSubarraySumCircular(self, nums):
        # Build circular linked list
        length = len(nums)
        if length == 0:
            return 0
        
        prevNode = Node(nums[0])
        self.first = prevNode
        for num in nums[1:]:
            myNode = Node(num)
            prevNode.next = myNode
            myNode.back = prevNode
            prevNode = myNode
        prevNode.next = self.first  # Make it circular

        # Initialize variables for Kadane's algorithm
        currNode = self.first
        currMax = float('-inf')
        globalMax = float('-inf')
        count = 0

        # First pass: Find the maximum subarray sum using Kadane's algorithm
        while count < length:
            currMax = max(currMax + currNode.value, currNode.value)
            globalMax = max(globalMax, currMax)
            currNode = currNode.next
            count += 1

        # Now, we need to find the minimum subarray sum
        currNode = self.first
        currMin = float('inf')
        globalMin = float('inf')
        count = 0

        # Second pass: Find the minimum subarray sum
        while count < length:
            currMin = min(currMin + currNode.value, currNode.value)
            globalMin = min(globalMin, currMin)
            currNode = currNode.next
            count += 1

        # Calculate total sum of the array
        total_sum = sum(nums)

        # The maximum circular subarray sum is total_sum - globalMin
        max_circular = total_sum - globalMin if total_sum != globalMin else globalMax

        # Return the maximum of the two cases
        return max(globalMax, max_circular)

# Example usage
myObject = Solution()
array = [5, -3, 5]
print(myObject.maxSubarraySumCircular(array))  # Output: 10
