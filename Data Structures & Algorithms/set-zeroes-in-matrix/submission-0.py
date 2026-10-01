class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        col = len(matrix[0])
        row = len(matrix)
        rowtrack = [0 for _ in range(row)]
        coltrack = [0 for _ in range(col)]
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    rowtrack[i] = -1
                    coltrack[j] = -1
        for i in range(row):
            for j in range(col):
                if rowtrack[i] == -1 or coltrack[j] == -1:
                    matrix[i][j] = 0
                    
        
        
        