class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        
        rows = len(grid)
        cols = len(grid[0])
        checkedArr = [[False for _ in range(cols)] for _ in range(rows)]
        num_islands = 0
        
        # Directions for moving up, down, left, right
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        def bfs(startRow, startCol):
            queue = [(startRow, startCol)]
            checkedArr[startRow][startCol] = True
            
            while queue:
                row, col = queue.pop(0)
                
                for dr, dc in directions:
                    newRow, newCol = row + dr, col + dc
                    
                    if 0 <= newRow < rows and 0 <= newCol < cols:
                        if grid[newRow][newCol] == "1" and not checkedArr[newRow][newCol]:
                            checkedArr[newRow][newCol] = True
                            queue.append((newRow, newCol))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and not checkedArr[r][c]:
                    num_islands += 1
                    bfs(r, c)  # Start BFS to mark all connected land

        return num_islands

# Example usage
myObject = Solution()
grid = [["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]]
print(myObject.numIslands(grid))  # Output: 1