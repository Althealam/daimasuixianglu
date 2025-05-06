# 时间复杂度：O(n)，其中n是nums的长度
# 空间复杂度：O(1)
class Solution:
    def jump(self, nums: List[int]) -> int:
        ans=0 # 跳跃的最少步数
        cur_right=0 # 已建造的桥的右端点
        next_right=0 # 下一座桥的右端点的最大值
        for i in range(len(nums)-1):
            # 遍历的过程中，记录下一座桥的最远点
            next_right=max(next_right, i+nums[i])
            if i==cur_right: # 无路可走，必须建桥
                cur_right=next_right 
                ans+=1
        return ans