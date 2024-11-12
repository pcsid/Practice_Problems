#INCOMPLETE

class Solution(object):
    def snakesAndLadders(self, board):
        #flatten board
        n = len(board)
        flattenedBoard = []
        count = 0
        for i in range(n):
            for j in range(n):
                count += 1
                if board[i][j] == -1:
                    flattenedBoard.append(count)
                else:
                    flattenedBoard.append(board[i][j])
        flattenedBoard.insert(0, 0)
        #bfs
        def bfs():
            
            shortest = float("inf")
            queue = [(1, 0)]
            visited = [False] * (n**2 + 1)
            visited[1] = True
            
            while(queue):
                curr, steps = queue.pop(0)
                
                # Check if we reached the last square
                if curr == n**2:
                    if shortest > steps:
                        shortest = steps
                
                # Explore the next 6 possible moves
                for i in range(1, 7):
                    next_pos = curr + i
                    if next_pos <= n**2:
                        # If there's a snake or ladder, move to its destination
                        if flattenedBoard[next_pos] != -1:
                            next_pos = flattenedBoard[next_pos]
                        
                        # If not visited, add to the queue
                        if not visited[next_pos]:
                            visited[next_pos] = True
                            queue.append((next_pos, steps + 1))
                            # Add the position after moving to a snake/ladder
                            if flattenedBoard[next_pos] != -1 and flattenedBoard[next_pos] != next_pos:
                                queue.append((flattenedBoard[next_pos], steps + 1))
            
            if shortest == float("inf"):
                return -1
            return shortest 
        
        return bfs()

# Example usage
myObject = Solution()
board = [[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]]
print(myObject.snakesAndLadders(board))