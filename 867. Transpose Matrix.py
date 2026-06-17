class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        newm=[[0]*len(matrix) for i in range(len(matrix[0]))]
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                newm[col][row]=matrix[row][col]
        return newm
