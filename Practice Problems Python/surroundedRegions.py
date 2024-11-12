class Solution(object):
    def solve(self, board):
        
        rows = len(board)
        cols = len(board[0])
        visited = [[False for i in range(cols)] for j in range(rows)]

        def safeBFS(currRow, currCol):
            queue = [(currRow, currCol)]
            dirs = [[0, -1],[-1, 0],[0,1],[1,0]]
            

            while len(queue) != 0:
                mySpot = queue.pop(0)
                startRow = mySpot[0]
                startCol = mySpot[1]
                visited[startRow][startCol] = True
                board[startRow][startCol] = "S"

                for dir in dirs:
                    currRow = startRow + dir[0]
                    currCol = startCol + dir[1]
                    if 0 <= currRow < rows and 0 <= currCol < cols and visited[currRow][currCol] == False:
                        if board[currRow][currCol] == "O":
                            board[currRow][currCol] = "S"
                            queue.append([currRow, currCol])
                            visited[currRow][currCol] = True
        #top row
        for i in range(cols):
            if (board[0][i] == "O"):
                safeBFS(0, i)
        #print(board)
        #left col
        for j in range(rows):
            if (board[j][0] == "O"):
                safeBFS(j, 0)
        #print(board)
        #bottom row
        for i in range(cols):
            if (board[rows-1][i] == "O"):
                safeBFS(rows - 1, i)
        #print(board)
        #right col
        for j in range(rows):
            if (board[j][cols-1] == "O"):
                safeBFS(j, cols - 1)

        #print(board)

        for i in range(0,rows):
            for j in range(0,cols):
                if board[i][j] == "O":
                    board[i][j] = "X"
                if board[i][j] == "S":
                    board[i][j] = "O"
        return(board)
    

    
myObject = Solution()
board = [["O","X","O"],["X","O","X"],["O","X","O"]]
print(myObject.solve(board))