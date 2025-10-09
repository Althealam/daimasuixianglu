class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums.sort()
        for i in range(len(nums)):
            if nums[i]<0 and k>0:
                nums[i] = -1*nums[i]
                k-=1
        
        nums.sort()
        while k>0:
            nums[0] = -1*nums[0]
            k-=1
        return sum(nums)
        