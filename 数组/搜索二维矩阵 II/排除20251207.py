
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        i, j = 0, n-1
        while i>=0 and i<m and j>=0 and j<n:
            if matrix[i][j]==target:
                return True
            elif matrix[i][j]<target: # 这一行的元素都比target小，因此直接剪去这一行
                i+=1
            else: # 这一列的元素都比target大，因此直接剪去这一行
                j-=1
        return False