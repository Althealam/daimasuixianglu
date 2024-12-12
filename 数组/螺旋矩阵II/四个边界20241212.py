# 思路：给定正整数n，那么就需要n^2个元素
# 先填充上边界，再填充右边界，再填充下边界，最后填充左边界
# 然后依次继续填充里面的内容

# 时间复杂度：O(n^2)
# 空间复杂度：O(n^2)
class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        matrix=[[0]*n for _ in range(n)]
        left=0
        right=n-1
        bottom=n-1
        top=0
        num=1 # 起始值
        while top<=bottom and left<=right:
            # 从左到右遍历上边界
            for i in range(left,right+1):
                matrix[top][i]=num
                num+=1
            top+=1
            # 从上到下遍历右边界
            for i in range(top,bottom+1):
                matrix[i][right]=num
                num+=1
            right-=1
            # 从右到左遍历下边界
            for i in range(right,left-1,-1):
                matrix[bottom][i]=num
                num+=1
            bottom-=1
            # 从下到上遍历左边界
            for i in range(bottom,top-1,-1):
                matrix[i][left]=num
                num+=1
            left+=1
        return matrix