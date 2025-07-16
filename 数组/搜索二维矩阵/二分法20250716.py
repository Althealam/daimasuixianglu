# 思路：每一行是递增的，并且每一行的第一个数大于前面一行的最后一个数，因此将矩阵每一行拼接在一起，可以得到一个递增数组
# 因此可以对该有序数组二分查找其target值的位置

# 时间复杂度：O(log(mn)) 相当于有一个mn个元素的数组
# 空间复杂度：O(1)
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix) # m行n列
        n = len(matrix[0])
        left, right = 0, m*n-1
        while left<=right:
            mid = (left+right)//2
            x = matrix[mid//n][mid%n]
            if x>target:
                right = mid-1
            elif x<target:
                left = mid+1
            else:
                return True
        return False