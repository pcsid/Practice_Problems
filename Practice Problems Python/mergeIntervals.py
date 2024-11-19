class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Step 1: Sort intervals by the starting point
        intervals.sort(key=lambda x: x[0])
        
        # Step 2: Initialize the result list
        returnList = []
        
        # Step 3: Iterate through the intervals
        for interval in intervals:
            # If the returnList is empty or there is no overlap, append the interval
            if not returnList or returnList[-1][1] < interval[0]:
                returnList.append(interval)
            else:
                # There is an overlap, merge the intervals
                returnList[-1][1] = max(returnList[-1][1], interval[1])
        
        return returnList
