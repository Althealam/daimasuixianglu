# 思路：交换学生座位到正确的位置上，比如i上坐的学生的学号是nums[i]，那么nums[i]需要坐的位置就是nums[nums[i]-1] 需要判断是否一致，如果不一致的话则交换位置。全部学生交换完毕后，寻找第一个学号和座位不匹配的学生即可
# 时间复杂度：O(n) 虽然写了一个二重循环，但是每次交换都会把一个学生换到正确的位置上，所以总交换次数最多为n
# 空间复杂度：O(1)
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            # 如果当前学生的学号在[1, n]中，但是真身没有坐在正确的座位上
            while 1<=nums[i]<=n and nums[i]!=nums[nums[i]-1]: # 注意学号是从1开始的
                # 交换nums[i]和nums[j]，其中j是i的学号
                j = nums[i]-1
                nums[i], nums[j] = nums[j], nums[i]
        
        # 找第一个学号和座位编号不匹配的学生
        for i in range(n):
            if nums[i]!=i+1:
                return i+1
        
        # 所有学生都坐在正确的位置上
        return n+1