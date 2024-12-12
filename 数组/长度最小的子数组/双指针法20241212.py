# 滑动窗口
# 1. 用一个min_len记录目前长度最小的子数组的长度，初始化为inf；定义一个cur_sum来记录当前的滑动窗口的值
# 2. 定义一个双指针i和j，i为滑动窗口的起始位置，j为滑动窗口的终止位置
# （1）先固定i，不停移动j，直到找到这个滑动窗口的值大于target的j，然后记录滑动窗口的长度，更新min_len
# （2）当滑动窗口的值大于target：将i向右边移动一位，记录值：如果滑动窗口的值小于target，则继续移动j；

# 时间复杂度：O(n)
# 空间复杂度：O(1)

class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        min_len=float('inf')
        i,j=0,0
        cur_sum=0
        for j in range(len(nums)):
            cur_sum+=nums[j]
            while cur_sum>=target:
                min_len=min(min_len,j-i+1)
                cur_sum-=nums[i]
                i+=1
        return min_len if min_len!=float('inf') else 0