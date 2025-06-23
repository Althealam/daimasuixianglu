# 1. 思路：计算当前窗口内的连续子数组的和，如果连续子数组的和大于0，则继续加下一个元素
# 如果当前连续子数组的和小于0，则重新开始
nums = list(map(int, input().split()))

def greedy(nums):
    result = float('-inf')
    count = 0 # 当前滑动窗口的连续子数组的和
    for i in range(len(nums)):
        count+=nums[i]
        if count>result:
            result = count
        if count<0:
            count =0
    return result
    