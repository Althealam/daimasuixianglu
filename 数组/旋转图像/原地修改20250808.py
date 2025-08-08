# 思路：
# 顺时针旋转90度，相当于位于(i, j)的元素去到(j, n-1-i)
# (i,j)->(j, i)->(j, n-1-i)

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        for row in matrix:
            row.reverse()
        