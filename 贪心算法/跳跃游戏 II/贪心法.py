# 分析：利用尽可能小的步数来增加我们的覆盖范围
# 每一步尽可能的去增加覆盖范围
# 时间复杂度：O(n)
# 空间复杂度：O(1)
class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==1: # 数组大小为1时，起点就是终点，已经达到了
            return 0
        cur=0 # 当前覆盖最远距离下标
        nxt=0 # 下一步覆盖最远距离下标
        result=0 # 记录走的最大步数
        for i in range(len(nums)):
            nxt=max(i+nums[i],nxt)
            if i==cur: # 遇到当前覆盖最远距离下标，此时需要进行一次跳跃
                result+=1 # 需要走下一步
                cur=nxt # 更新当前覆盖最远距离
                if nxt>=len(nums)-1: # 当前覆盖最远距离达到数组末尾，不用再做result++操作，直接结束，已经跳到终点了
                    break
        return result
        