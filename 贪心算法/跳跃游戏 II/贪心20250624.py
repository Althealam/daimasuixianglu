# 思路：每次都尽量多跳跃一些距离，就可以让总的步数少一点
# 每次都记录cur_distance和next_distance，分别表示当前可以跳跃的最远距离，和下一个可以跳跃的最远距离

nums = list(map(int, input().split()))


def greedy(nums):
    cnt = 0 # 统计到达最后一步需要跳跃的步数
    cur_distance = 0 # 当前可以跳跃的最远距离
    next_distance = 0  # 下一步可以跳跃的最远距离
    for i in range(len(nums)-1): # 注意这里是len(nums)-1
        next_distance = max(next_distance, nums[i] + i) # 下一步可以跳跃的最远距离
        if i==cur_distance:
            cur_distance = next_distance
            cnt+=1
    return cnt