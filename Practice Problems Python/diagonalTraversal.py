#top left to bottom right
def traverseDiagonals(matrix):
    if not matrix:
        return []
    
    rows, cols = len(matrix) - 1, len(matrix[0]) - 1
    result = []

    # Traverse diagonals based on the sum of row and column indices (i + j)
    for diagonal_index in range(rows + cols + 1):
        diagonal = []
        #the +1 is for range(exlcusive on second num)
        for i in range(max(0, diagonal_index - cols), min(diagonal_index, rows) + 1):
            j = diagonal_index - i
            diagonal.append(matrix[i][j])     
        result.append(diagonal)
    return result

# Example usage
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12]
]

# Print the diagonals
diagonals = traverseDiagonals(matrix)
for diagonal in diagonals:
    print(diagonal)
