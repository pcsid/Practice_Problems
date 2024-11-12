class Solution(object):
    def minPathSum(self, grid):
        m = len(grid) - 1
        n = len(grid[0]) - 1

        diagonals = m + n
        for diagonal in range(diagonals, -1, -1):
            #print(min(diagonal,m))
            #print(max(diagonal-m,0))
            for row in range(min(diagonal, m), max(diagonal - n, 0) - 1, -1):
                col = diagonal - row
                #not last cell
                #print(grid[row][col])
                if row + col == diagonals:
                    break
                if row + 1 > m:
                    grid[row][col] += grid[row][col + 1]
                elif col + 1 > n:
                    grid[row][col] += grid[row + 1][col]
                else:
                    grid[row][col] += min(grid[row][col + 1], grid[row + 1][col])
                #print(f"row {row} col {col} value {grid[row][col]}")
        return(grid[0][0])

        

gridTest = [[1,2,3],[4,5,6],[7,8,9]]
grid = [[1,3,1],[1,5,1],[4,2,1]]
gridTest2 = [[1,2,3],[4,5,6]]

myObject = Solution()
print(myObject.minPathSum(gridTest2))