class Solution(object):
    def isValidSudoku(self, board):
        #check rows
        for row in board:
            print(row)
            rowCheck = []
            for num in row:
                if num.isnumeric():
                    if num in rowCheck:
                        print("broke at row")
                        return False
                    else:
                        rowCheck.append(num)
        for col in range(9):
            colCheck = []
            for row in board:
                #print(type(row[col]))
                if row[col].isnumeric():
                    if row[col] in colCheck:
                        print("broke at col")
                        return False
                    else:
                        colCheck.append(row[col])
        colStart = 0
        colEnd = 2
        for i in range(3):
            rowStart = 0
            rowEnd = 2
            
            for j in range(3):
                
                squareCheck = []
                for row in range(rowStart, rowEnd + 1):
                    for col in range(colStart, colEnd + 1):
                        if board[row][col].isnumeric():
                            if board[row][col] in squareCheck:
                                #print(f"broke at {i} - {j}")
                                print("broke at grid")
                                return False
                            else:
                                squareCheck.append(board[row][col])
                rowStart += 3
                rowEnd += 3

            colStart += 3
            colEnd += 3

        return True
    
myObject = Solution()
board = [[".",".",".",".","5",".",".","1","."],[".","4",".","3",".",".",".",".","."],[".",".",".",".",".","3",".",".","1"],["8",".",".",".",".",".",".","2","."],[".",".","2",".","7",".",".",".","."],[".","1","5",".",".",".",".",".","."],[".",".",".",".",".","2",".",".","."],[".","2",".","9",".",".",".",".","."],[".",".","4",".",".",".",".",".","."]]
print(myObject.isValidSudoku(board))