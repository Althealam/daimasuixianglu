# 思路：
# 有四个边界值，分别是left, right, top, bottom
# 先填充上边界，再填充右边界，再填充下边界，最后填充左边界
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        result=[[0]*n for _ in range(n)]
        top, bottom, left, right = 0, n-1, 0, n-1
        num = 1 # 当前遍历的元素值
        while left<=right and top<=bottom:
            for j in range(left, right+1): # 1->2->3
                result[top][j]=num
                num+=1
            top+=1
            for i in range(top, bottom+1): # 4->5
                result[i][right]=num
                num+=1
            right-=1
            for j in range(right, left-1, -1): # 6->7
                result[bottom][j]=num
                num+=1
            bottom-=1
            for i in range(bottom, top-1, -1): # 8
                result[i][left]=num
                num+=1
            left+=1
        return result

