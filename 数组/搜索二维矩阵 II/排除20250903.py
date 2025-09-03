class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        i, j = 0, n-1
        while i<m and j>=0:
            if matrix[i][j]==target:
                return True
            if matrix[i][j]<target: # 这一行的剩余元素全部小于target
                i+=1
            else: # 这一列的剩余元素全部大于target
                j-=1
        return False
        