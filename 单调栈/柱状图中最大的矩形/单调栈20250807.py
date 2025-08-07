# 1. 求当前柱子左边和右边第一个比他矮的柱子，以此来求宽度right-left-1
# 2. 单调栈中存储还没找到下一个更小元素的元素下标
# 3.（1）如果nums[i]<=nums[st[-1]]找到了下一个更小元素的元素下标，则right=i，弹出栈顶元素并且加入当前元素（单调栈是递减的）
#   （2）如果nums[i]>nums[st[-1]]则当前元素i的左边的第一个更小元素下标为st[-1]
# 4. 求出每个元素的右边/左边的第一个最大元素 根据这两个元素值计算面积
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        ans = 0
        left = [0]*len(heights)
        right = [len(heights)]*len(heights)
        st = []
        for i in range(len(heights)):
            while len(st)!=0 and heights[i]<=heights[st[-1]]: # 栈顶元素找到了右边的第一个更小元素
                right[st[-1]] = i
                st.pop()
            if len(st)!=0 and heights[i]>heights[st[-1]]:
                left[i]=st[-1]
            st.append(i)
        
        for h, l, r in zip(heights, left, right):
            ans = max(ans, h*(r-l-1))
        return ans
