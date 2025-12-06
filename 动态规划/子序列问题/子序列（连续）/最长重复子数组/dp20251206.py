# 1. definition: dp[i][j] is the maximal length of a subarray that ends with nums1[i-1] and nums2[j-1]
# 2. formula:
# if nums1[i]==nums2[j]: dp[i][j] = max(dp[i-1][j-1]+1, dp[i][j])
# 3. initialization: dp = [[0]*(len(nums2)+1) for _ in range(len(nums1)+1)]
# we can not use dp=[[0]*(len(nums2)) for _ in range(len(nums1))] cause we need to get the dp[i-1][j-1]
# 4. order: nums1 first then nums2
class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        dp = [[0]*(len(nums2)+1) for _ in range(len(nums1)+1)]
        res = 0
        for i in range(1, len(nums1)+1):
            for j in range(1, len(nums2)+1):
                if nums1[i-1]==nums2[j-1]:
                    dp[i][j]=max(dp[i-1][j-1]+1, dp[i][j])
                res = max(res, dp[i][j])
        return res 

