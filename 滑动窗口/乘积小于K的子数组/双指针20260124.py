from re import S
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k<=1:
            return 0
        product_sum = 1
        left = 0
        ans = 0
        for right in range(len(nums)):
            product_sum*=nums[right]
            while product_sum>=k:
                product_sum/=nums[left]
                left+=1
            ans+=right-left+1 # 以right为结尾的子数组的个数
            
        return ans


nums = [10,5,2,6]
k = 100
solution = Solution()
res = solution.numSubarrayProductLessThanK(nums, k)
print(res)
