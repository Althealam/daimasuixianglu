# 思路：
# 有四个边界值，分别是left, right, top, bottom
# 先填充上边界，再填充右边界，再填充下边界，最后填充左边界
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        # 生成矩阵
        result=[[0]*n for _ in range(n)]
        # 定义边界值
        left=0
        right=n-1
        top=0
        bottom=n-1
        # 定义元素值
        num=1 
        while top<=bottom and left<=right:
            # 填充上边界
            for j in range(left, right+1):
                result[top][j]=num
                num+=1
            top+=1
            # 填充右边界
            for i in range(top, bottom+1):
                result[i][right]=num
                num+=1
            right-=1
            # 填充下边界
            for j in range(right, left-1, -1):
                result[bottom][j]=num
                num+=1
            bottom-=1
            # 填充左边界
            for i in range(bottom, top-1, -1):
                result[i][left]=num
                num+=1
            left+=1
        return result
