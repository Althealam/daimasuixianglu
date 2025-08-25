# 思路：贪心法，每次都尽量跳尽可能多的距离
class Solution:
    def jump(self, nums: List[int]) -> int:
        step = 0 # 总共要跳的数字
        cur_distance = 0  # 当前跳跃的距离
        next_distance = 0  # 下一次跳跃的距离
        for i in range(len(nums)-1):
            next_distance = max(next_distance, nums[i]+i)
            if i==cur_distance:
                cur_distance = next_distance
                step+=1
        return step
        