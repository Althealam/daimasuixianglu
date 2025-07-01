# 分析：
# 已知数组会被拆分为两段，并且这两段数组都是递增的
# 1. 如果target>nums[n-1]，那么target在第一段数组中，也就是[0, i-1]中 并且i对应的就是最小值
# 2. 如果target<nums[n-1]，那么target在第二段数组中，也就是[i, n-1]中
# （2.1）i=0: nums是递增的，直接在[0, n-1]中二分查找
# （2.2）i>0: target一定在[i, n-1]中，在[i, n-1]中二分查找

# 思路：1. 找到数组的最小值，这个最小值的下标就是i 2. 根据上述分析找到target在哪一段中 3. 二分查找

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        min_num_index = self.find_min(nums) # i的下标
        if target>nums[-1]: # target在nums[:i-2]中
            return self.erfenchazhao(nums, target, left = 0, right = min_num_index-1) 
        else:
            return self.erfenchazhao(nums, target, left = min_num_index, right = len(nums)-1)


    def erfenchazhao(self, nums, target, left, right):
        """在给定的数组nums中查找target的下标"""
        while left<=right: # 闭区间[left, right]
            mid = (left+right)//2
            if nums[mid]>target: # target在[left, mid-1]中
                right = mid-1
            elif nums[mid]<target: # target在[mid+1, right]中
                left = mid+1
            else:
                return mid
        return -1
    
    def find_min(self, nums):
        min_num = float('inf')
        min_num_index = 0
        for i in range(len(nums)):
            min_num = min(min_num, nums[i])
            if min_num==nums[i]:
                min_num_index = i
        return min_num_index 

