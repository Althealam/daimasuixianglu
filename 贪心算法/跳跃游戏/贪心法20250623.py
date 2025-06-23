# 思路：
# 1. 遍历数组nums，获取目前为止可以跳跃到达的最大位置：cover = max(cover, i+nums[i])
# 2. 每次跳跃的时候都判断i是否在cover内：if i>=cover: return False
# 3. 当cover>=len(nums)-1时则返回True
nums = list(map(int, input().split()))


def greedy(nums)
    cover = 0 # 计算当前可覆盖的最远位置
    for i in range(len(nums)):
        if i<=cover:
            cover = max(cover, i+nums[i]) # 更新可以跳跃的最远范围
        else:
            return False
        if cover>=len(nums)-1:
            return True
    return False
        