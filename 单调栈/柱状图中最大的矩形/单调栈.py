# 分析：本题就是找左边第一个比他矮的，再找右边第一个比他矮的，这两个柱子可以确定宽度
# 本题和接雨水是相反的，并且单调栈是使用递减的（递减可以保证是求右边第一个比他小的）
# 栈顶和栈顶的下一个元素以及要入栈的元素组成了我们要求最大面积的高度和宽度

# 时间复杂度：O(n)
# 空间复杂度：O(n)
class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        heights.insert(0,0)
        heights.append(0)
        stack=[0]
        result=0
        for i in range(1,len(heights)):
            while stack and heights[i]<heights[stack[-1]]:
                mid_height=heights[stack[-1]]
                stack.pop()
                if stack:
                    area=(i-stack[-1]-1)*mid_height
                    result=max(area,result)
            stack.append(i)
        return result
        