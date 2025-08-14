# 贪心策略：如果x+y>y+x，那么x>y；如果x+y<y+x，那么x<y
# 两个数字对应的字符串a和b，如果字典序a+b>b+a，此时a排在b前面可以获得更大值
# 比如a=3，b=32，那么两者拼接的值是332>323，因此3应该排在32的前面
# 时间复杂度：O(n^2)
# 空间复杂度：O(n)
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        n = len(nums)
        nums = list(map(str, nums))
        for i in range(n):
            for j in range(i+1, n):
                if nums[i]+nums[j]<nums[j]+nums[i]:
                    nums[i], nums[j] = nums[j], nums[i]
        return str(int("".join(nums)))