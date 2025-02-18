# 局部最优：让绝对值大的负数变成正数
# 全局最优：整个数组和达到最大
# 思路：
# 1. 遍历nums，排序nums
# 2. 将负数变成正数，并且k-=1
# 3. 排序nums，如果k还没用完，则将nums中最小的数反复变化，并且k-=1
# 4. 如果k已经用完了，则直接返回sum(nums)

# 时间复杂度：O(nlogn)
# 1. 排序操作：O(nlogn)
# 2. 便利操作：O(n)
# 3. while操作：O(k)
# 4. 求和操作：O(n)

# 空间复杂度：O(1)

class Solution(object):
    def largestSumAfterKNegations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        for i in range(len(nums)):
            # 将负数变成正数
            if k>0 and nums[i]<0:
                nums[i]=-1*nums[i]
                k-=1

        nums.sort()
        while k>0:
            nums[0]=-1*nums[0]
            k-=1
        return sum(nums)
            


        