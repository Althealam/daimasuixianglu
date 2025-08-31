# 1. dp数组以及下标的含义：dp[i][j]表示以nums1[i-1]为为结尾和以nums2[j-1]为结尾的最长重复子串长度
# 2. 递推公式：
# if nums1[i-1]==nums2[j-1]: dp[i][j] = dp[i-1][j-1]+1
# 3. 初始化：全部初始化为0
class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        dp = [[0]*(len(nums2)+1) for _ in range(len(nums1)+1)]
        res = 0
        for i in range(1, len(nums1)+1):
            for j in range(1, len(nums2)+1):
                if nums1[i-1]==nums2[j-2]:
                    dp[i][j] = dp[i-1][j-1]+1
                res = max(res, dp[i][j])
        return res
        