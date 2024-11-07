# 双指针法
# 思路：定义slow和fast，slow指向窗口的左索引，fast指向窗口的右索引
# fast逐渐向右遍历，然后计算slow到fast之间的元素的累加值cur_sum，当累加值大于target以后，就记录当前的窗口长度，然后将cur_sum减去slow的值，并且将slow指针向右边移动一位
# 这样可以避免让fast指针重新从slow指针开始进行遍历
class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        slow=0
        fast=0
        min_length=float('inf') # 初始化最小窗口的长度值
        cur_sum=0
        # 移动右指针
        for fast in range(len(nums)):
            cur_sum+=nums[fast]
            while cur_sum>=target:
                min_length=min(min_length,fast-slow+1)
                cur_sum-=nums[slow]
                slow+=1
        return 0 if min_length==float('inf') else min_length





