# 单调栈
# 接雨水是找每个柱子左右两边第一个大于该柱子高度的柱子，而本题是找每个柱子左右两边第一个小于该柱子高度的柱子
# 接雨水的单调栈是从小到大，而本题的单调栈是从大到小
# 1. 当前遍历的元素height[i]大于栈顶元素height[stack[-1]]: stack.append(i)
# 2. 当前遍历的元素height[i]小于栈顶元素height[stack[-1]]
# 3. 当前遍历的元素height[i]等于栈顶元素height[stack[-1]]: stack.pop() stack.append(i)
# 注意：本题的首尾的两个柱子可以作为核心柱进行尝试

# 时间复杂度：O(n)
# 空间复杂度：O(n) 最坏情况下栈需要存储所有的元素，比如当输入的元素是递增的时候，所有元素都会依次入栈

class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        heights.insert(0,0) # 在开头插入0元素
        heights.append(0) # 在结尾插入0元素
        stack=[0]
        result=0
        for i in range(1, len(heights)):
            # 情况1：当前柱子的高度大于栈顶柱子的高度，说明当前柱子可以作为一个更高的矩形的一部分继续向右扩展
            # 将当前柱子的索引压入栈中，继续维护单调递增的栈
            if heights[i]>heights[stack[-1]]:
                stack.append(i)
            # 情况2：当前柱子的高度等于栈顶柱子的高度，由于高度相同，因此栈顶柱子对后续计算最大矩形面积没有帮助
            # 将栈顶元素弹出，将当前柱子的索引压入栈中
            elif heights[i]==heights[stack[-1]]:
                stack.pop()
                stack.append(i)
            # 情况3：当前柱子的高度小于栈顶柱子的高度，说明栈顶柱子不能再向右扩展了，需要计算以栈顶柱子为高的矩形面积
            else:
                # 找出所有较高的柱子
                while stack and heights[i]<heights[stack[-1]]:
                    # 栈顶就是中间的柱子，主心骨
                    mid_index=stack[-1]
                    stack.pop()
                    if stack:
                        left_index=stack[-1]
                        right_index=i
                        w=right_index-left_index-1
                        h=heights[mid_index]
                        result=max(result, w*h)
                stack.append(i)
        return result


        