class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        
        rows = len(obstacleGrid) - 1
        cols = len(obstacleGrid[0]) - 1

        if obstacleGrid[0][0] == 1 or obstacleGrid[rows][cols] == 1:
            return 0

        diagonals = rows + cols
        pathGrid = []
        for i in range(rows + 1):
            row = []
            for j in range(cols + 1):
                row.append(0)
            pathGrid.append(row)
        pathGrid[rows][cols] = 1
        #print(pathGrid)
        for diagonal in range(diagonals, -1, -1):
            for row in range(min(diagonal, rows), max(diagonal - cols, 0) - 1, -1):
                col = diagonal - row
                if row + col == diagonals or obstacleGrid[row][col] == 1:
                    continue
                if row + 1 > rows:
                    pathGrid[row][col] = pathGrid[row][col + 1]
                elif col + 1 > cols:
                    pathGrid[row][col] = pathGrid[row + 1][col]
                else:
                    pathGrid[row][col] = pathGrid[row + 1][col] + pathGrid[row][col + 1]
                #print(f"row: {row} col: {col} value: {pathGrid[row][col]}")
        return pathGrid[0][0]
                #if row + 1 > rows:
                    #obstac

myObject = Solution()
obstacleGrid = [[0,0]]
print(myObject.uniquePathsWithObstacles(obstacleGrid))