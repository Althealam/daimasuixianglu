# 分析：用一个数组记录每个元素右边比他高的柱子是哪一个，再用一个数组记录每个元素左边比他高的柱子是哪个
# 大体思路：
# 1. 当前遍历元素>栈口元素：当前遍历的元素就是右边的第一个比他大的元素（左边第一个比他大的元素就在栈里，也就是该元素在栈里的右边第二个元素）
# 一旦发现添加的柱子高度大于栈头元素了，此时就出现凹槽了，栈头元素就是凹槽底部的柱子，栈头第二个元素就是凹槽左边的柱子，而添加的元素就是凹槽右边的柱子
# 2. 当前遍历元素<=栈口元素：将该元素入栈
# 高度：假设左边高的元素为i，右边高的元素为j，高度为height[i]和height[j]的最小值，并且减去当前的元素的height
# 宽度就是j-i-1
# 这时候高度x宽度就是雨水的面积

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # stack储存index，用于计算对应的柱子高度
        stack=[0]
        result=0
        for i in range(1,len(height)):
            while stack and height[i]>height[stack[-1]]: # 出现凹槽
                mid_height=stack.pop() # 遇到凹槽，弹出元素
                if stack:
                    # 雨水高度是min（凹槽左侧高度，凹槽右侧高度）-凹槽底部高度
                    # stack[-1]代表的是栈中最后一个元素
                    h=min(height[stack[-1]],height[i])-height[mid_height]
                    # 雨水宽度是 凹槽右侧的下标-凹槽左侧的下标-1
                    w=i-stack[-1]-1
                    # 累计总雨水体积
                    result+=h*w
            stack.append(i)
        return result