# 双指针法
# 思路：计算每个位置能接住的雨水量，关键在于明确该位置左右两侧的最大柱子高度。
# 该位置能接住的雨水量等于其左右两侧最大高度中的较小值减去当前位置柱子的高度
# 因此，我们可以分别计算出每个位置左侧和右侧的最大柱子高度，然后根据上述规则计算每个位置的雨水量

# 时间复杂度：O(n) 遍历height
# 空间复杂度：O(n) leftheight和rightheight
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        leftheight, rightheight=[0]*len(height), [0]*len(height)

        # 计算每个位置左侧的最大柱子高度
        leftheight[0]=height[0]
        for i in range(1, len(height)):
            leftheight[i]=max(leftheight[i-1], height[i])
        # 计算每个位置右侧的最大柱子高度
        rightheight[-1]=height[-1]
        for i in range(len(height)-2, -1, -1):
            rightheight[i]=max(rightheight[i+1], height[i])
        # 计算每个位置能接住的雨水量并累加
        result=0
        for i in range(0, len(height)):
            # 能接住的雨水量等于该位置左右两侧高度中的较小值，减去当前位置柱子的高度height[i]
            summ=min(leftheight[i], rightheight[i])-height[i]
            result+=summ
        return result