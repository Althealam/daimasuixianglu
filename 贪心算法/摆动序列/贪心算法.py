# 分析：本题要求通过从原始序列中删除一些（也可以不删除）元素来获得子序列，剩下的元素保持其原始顺序
# 1. 局部最优：删除单调坡度上的节点（不包括单调坡度两端的节点），那么泽哥坡度就可以有两个局部峰值
# 2. 整体最优：整个序列有最多的局部峰值，从而达到最长摆动序列
# 思路：三种情况
# 1. 情况一：上下坡中有平坡[1,2,2,2,1]--删除左边的三个2
# 2. 情况二：数组首尾两端[2,5]--假设为[2,2,5]--这种情况result初始化为1，默认最右边有一个峰值
# 3. 情况三：单调坡中有平坡
class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)<=1:
            return len(nums)
        curDiff=0 # 当前一对元素的差值
        preDiff=0 # 前一对元素的差值
        result=1 # 记录峰值的个数，初始化为1（默认最右边的元素被视为峰值）
        for i in range(len(nums)-1):
            curDiff=nums[i+1]-nums[i] # 计算下一个元素与当前元素的差值
            # 出现摆动时再去更新摆动变化，就可以避免单调坡中有平坡的情况
            if (preDiff<=0 and curDiff>0) or (preDiff>=0 and curDiff<0):
                result+=1 # 峰值个数加1
                preDiff=curDiff # 只在摆动变化的时候更新preDiff
        return result
        