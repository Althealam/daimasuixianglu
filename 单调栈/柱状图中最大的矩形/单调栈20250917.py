# 1. 通过求该柱子左边和右边第一个比它矮的柱子，由此来求宽度right-left-1
# （1）如果i左侧的小于h的最近元素的下标left，如果不存在则为-1.当求出了left之后，left+1就是矩形最左边的那根柱子
# （2）如果i右侧的小于h的最近元素的下标right，如果不存在则为n，当求出了right之后，right-1就是矩形最右边的那根柱子
# 2. 通过柱子的基准来确定高度h
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        left = [-1]*n # 左边的第一个比它矮的柱子
        right = [n]*n # 右边的第一个比它矮的柱子
        st = []
        for i in range(len(heights)):
            while st and heights[i]<=heights[st[-1]]:
                right[st.pop()] = i
            if st: # 当前元素比栈顶元素要大，说明栈顶元素是该元素左边的第一个小柱子
                left[i] = st[-1]
            st.append(i)
        
        ans = 0
        for h, l, r in zip(heights, left, right):
            ans = max(ans, h*(r-l-1))
        return ans
        