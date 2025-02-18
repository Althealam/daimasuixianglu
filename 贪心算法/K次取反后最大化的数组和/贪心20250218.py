# 局部最优：让绝对值大的负数变成正数
# 全局最优：整个数组和达到最大
# 思路：
# 1. 遍历nums
# 2. 将负数变成正数，并且k-=1
# 3. 如果k还没用完，则将nums中最小的数反复变化
# 4. 如果k在所有负数没有变化完时就用完了也没关系，因为此时剩下的都是数值比较小的负数

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
            


        