class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool: 
        m, n = len(matrix), len(matrix[0])
        left, right = 0, m*n-1
        while left<=right: # 这里一定是left<=right而不是left<right，否则当只剩下一个元素的时候，会退出循环
            mid = (left+right)//2
            x = matrix[mid//n][mid%n]
            if x==target:
                return True
            elif x>target:
                right-=1
            else:
                left+=1
        return False