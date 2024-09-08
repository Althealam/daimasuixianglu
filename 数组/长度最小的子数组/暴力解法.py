# 方法一：暴力解法
# 输入：含有n个正整数的数组和一个正整数s
# 输出：其和>=s的长度最小的连续子数组的长度
# 解法：两层循环遍历数组，外层循环确定子数组的起始位置，内层循环确定子数组的结束位置
# 当找到一个满足条件的子数组时，更新最小长度min_length；如果遍历完整个数组都没有找到满足条件的子数组，则返回0
# 例子：target=7
# nums=[2,3,1,2,4,3]
# 外层循环从i=0开始，遍历数组nums
# 当i=0时：
#   初始化current_sum=0
#       内层循环从j=0开始，尝试找到满足条件的最小长度子数组
#           j=0, current_sum=2
#           j=1, current_sum=5
#           j=2, current_sum=6
#           j=3, current_sum=8>target, window_length=4
#           j=4, current_sum=12, window_length=2 更新min_length=2
#       内层循环结束，i增加到1
#       以此类推，直到i=n-1
class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        min_len=float('inf') # 初始化为无穷大
        for i in range(n): 
            cur_sum=0 # 当前窗口的和
            # 遍历数组，找到满足条件的最小长度子数组
            for j in range(i,n):
                cur_sum+=nums[j]
                # 当窗口和大于等于target时，尝试更新最小长度
                if cur_sum>=target:
                    # 计算当前窗口的长度
                    window_length=j-i+1
                    # 更新最小长度
                    min_len=min(min_len,window_length)
                    # 尝试缩小窗口，以找到更小的满足条件的子数组
                    cur_sum-=nums[i]
                    i+=1
                    break
        return 0 if min_len==float('inf') else min_len