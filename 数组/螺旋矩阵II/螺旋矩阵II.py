# 输入：n
# 输出：一个包含1到n^2的所有元素，且元素按照顺时针顺序螺旋排列
# 时间复杂度：O(n^2) while循环会持续进行直到填充完所有nxn个元素
# 空间复杂度：O(n^2) 填充一个nxn矩阵的所有元素
# 分析：填充矩阵的方式是上、右、下、左
class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        matrix=[[0]*n for _ in range(n)] # 创建一个nxn的全零矩阵
        num=1 # 从数字1开始
        top, bottom, left, right=0, n-1, 0, n-1 # 初始化边界
        while num<=n*n:
            # 填充矩阵的上边缘
            for i in range(left, right+1): # 从左到右
                # range是左闭右开的
                matrix[top][i]=num
                num+=1
            top+=1

            # 填充矩阵的右边界
            for i in range(top, bottom+1): # 从上到下
                matrix[i][right]=num
                num+=1
            right-=1 # 如果right>1的话，就会准备填充内部

            # 填充矩阵的下边缘
            if top<=bottom:
                for i in range(right, left-1, -1): # 从右到左
                    matrix[bottom][i]=num
                    num+=1
                bottom-=1
            
            # 填充矩阵的左边界
            if top<=bottom:
                for i in range(bottom, top-1, -1): # 从下到上
                    matrix[i][left]=num
                    num+=1
                left+=1
        return matrix