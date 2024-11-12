import heapq

class KthLargest:

    def __init__(self, k, nums):
        self.minHeap, self.k = nums, k
        heapq.heapify(self.minHeap)
        while len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        
    def add(self, val: int) -> int:
       heapq.heappush(self.minHeap, val)
       if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
       return self.minHeap[0]

k = 3
nums = [4, 5, 8, 2]
myObject = KthLargest(k, nums)
print(myObject.add(10))
print(myObject.add(3))