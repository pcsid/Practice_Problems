class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        rows = len(matrix)
        cols = len(matrix[0])
        matrix2 = [[0 for i in range(rows)] for j in range(cols)]
        for row in range(rows):
            for col in range(cols):
                matrix2[col][row] = matrix[row][col]
        return matrix2
        