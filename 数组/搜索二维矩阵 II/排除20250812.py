class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        i, j = 0, n-1 # 从右上角开始寻找
        while i<m and j>=0: # 还有剩余元素
            if matrix[i][j]==target:
                return True
            if matrix[i][j]<target:
                i+=1 # 这一行的剩余元素全部小于target
            else:
                j-=1 # 这一列的剩余元素全部大于target
        return False

        