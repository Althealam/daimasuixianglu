# 思路：每一行是递增的，并且每一行的第一个数大于前面一行的最后一个数，因此将矩阵每一行拼接在一起，可以得到一个递增数组
# 因此可以对该有序数组二分查找其target值的位置

# 时间复杂度：O(log(mn)) 相当于有一个mn个元素的数组
# 空间复杂度：O(1)
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix) # 行数
        n = len(matrix[0]) # 列数
        # 左闭右闭区间
        left = 0
        right = m*n-1 
        while left<=right:
            mid = (left+right)//2
            x = matrix[mid//n][mid%n] # 行为mid//n，列卫mid%n
            if x==target:
                return True
            if x<target: # target在[mid+1, right]中
                left = mid+1
            else:
                right = mid-1 # target在[left, mid-1]中
        return False # 没能找到target值