# 局部最优：每一步都尽可能的多走
# 全局最优：到达终点的步数最少
# 第i个位置能跳到的位置是:[i+1, i+nums[i]]
# 第0个位置可以跳到：[0+1, 0+nums[0]]=[1, nums[0]]
# 第1个位置可以跳到：[1+1, 1+nums[1]]=[2, 1+nums[1]]

# 维护几个变量：当前所能到达的最远位置end, 下一步能跳到的最远位置max_pos，最少跳跃次数steps
# 遍历数组nums的前面len(nums)-1个元素
# （1）更新第i位置下一步能跳到的最远位置max_pos=max(maxPos, nums[i]+i)
# （2）如果索引i到达了end边界，则更新end为max_pos，并steps+=1
# 返回跳跃次数steps

# 时间复杂度：O(n)
# 空间复杂度：O(1)

class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        max_pos=0 # 下一步能跳到的最远范围
        step=0 # 最小跳跃次数，返回值
        end=0 # 当前能跳到的最远范围
        for i in range(n-1):
            max_pos=max(max_pos, nums[i]+i)
            if i==end:
                end=max_pos
                step+=1
        return step