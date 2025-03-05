# 1. 单调栈是按照行方向来计算雨水
# 2. 单调栈内的顺序是从小到大的顺序（因为一旦发现柱子的高度大于栈头元素，就出现了凹槽）
# 3. 遇到相同高度的柱子，就更新栈内下标，弹出栈里的元素，将新元素加入栈中
# 4. 栈内保存的数值是下标（通过长*宽来计算雨水面积，长是柱子的高度，宽是通过柱子的下标来计算的）

# 单调栈的处理逻辑：
# 1. 当前遍历的元素高度小于栈顶元素的高度 height[i]<height[stack[-1]]：加入元素stack.append(i)
# 2. 当前遍历的元素高度等于栈顶元素的高度 height[i]==height[stack[-1]]：弹出栈顶元素，重新加入当前元素 
# 3. 当前遍历的元素高度大于栈顶元素的高度 height[i]>height[stack[-1]]：开始接于是

# 通过三个元素来接水：栈顶、栈顶的下一个元素，以及即将入栈的元素
# 雨水高度：min(凹槽左边高度，凹槽右边高度)-凹槽底部高度
# 雨水宽度：凹槽右边的下标-凹槽左边的下标-1（因为只求中间的宽度）


# 时间复杂度：O(n)，其中n是柱子的数量，每个柱子最多入栈和出栈一次
# 空间复杂度：O(n)，主要是栈的空间开销，最坏情况下需要存储所有柱子的索引
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        stack=[0] # 存储index，用于计算对应的柱子高度
        result=0 # 记录雨水的量
        for i in range(1, len(height)):
            # 情况1：当前遍历的元素高度小于栈顶元素的高度
            # 当前柱子的高度小于栈顶柱子的高度，说明当前柱子无法形成凹槽来接雨水，将当前柱子的索引压入栈中，继续维护单调递减的栈
            if height[i]<height[stack[-1]]:
                stack.append(i)
            
            # 情况2：当前遍历的元素高度等于栈顶元素的高度
            # 当前柱子的高度等于栈顶柱子的高度，由于高度相同，栈顶柱子对后续计算雨水量没有帮助，将栈顶元素弹出，将当前柱子的索引压入栈中
            elif height[i]==height[stack[-1]]:
                stack.pop()
                stack.append(i)
            
            # 情况3：当前遍历的元素高度大于栈顶元素的高度（开始接雨水）
            # 当前柱子的高度大于栈顶柱子的高度，说明形成了一个凹槽，可以开始计算雨水量
            else: 
                # 抛出所有较低的柱子
                while stack and height[i]>height[stack[-1]]:
                    # 每次弹出栈顶元素的时候，该元素对应的柱子就是凹槽的底部
                    mid_height=height[stack[-1]]
                    stack.pop()
                    if stack:
                        right_height=height[i] # 右侧的柱子
                        left_height=height[stack[-1]] # 左侧的柱子
                        # 两侧的比较矮的一方的高度-凹槽底部的高度
                        h=min(right_height, left_height)-mid_height
                        # 凹槽右侧下标-凹槽左侧下标-1：求解中间的宽度
                        w=i-stack[-1]-1
                        # 计算雨水体积
                        result+=h*w
                stack.append(i)
        return result

        