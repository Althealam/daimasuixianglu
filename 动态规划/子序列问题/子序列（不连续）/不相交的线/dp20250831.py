# 1. dp数组以及下标的含义：dp[i][j]表示以[0, i-1]的nums1和[0, j-1]的nums2的最长公共子序列的长度是dp[i][j]
# 2. 递推公式
# if nums1[i-1]==nums2[j-1]: dp[i][j] = dp[i-1][j-1]+1
# else: dp[i][j] = max(dp[i-1][j], dp[i][j-1])
# 3. 初始化：全部初始化为0
# 4. 遍历顺序：先遍历nums1，后遍历nums2

class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        dp = [[0]*(len(nums2)+1) for _ in range(len(nums1)+1)]
        res = 0
        for i in range(1, len(nums1)+1):
            for j in range(1, len(nums2)+1):
                if nums1[i-1]==nums2[j-1]:
                    dp[i][j] = dp[i-1][j-1]+1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
                res = max(res, dp[i][j])
        return res