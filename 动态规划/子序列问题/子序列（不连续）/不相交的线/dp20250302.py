# 本题其实就是最长公共子序列

# 1. dp数组以及下标的含义：[0,i-1]的num1和[0,j-1]的nums2的最长公共子序列长度为dp[i][j1]
# 2. 递推公式
# （1）nums1[i-1]==nums2[j-1]: dp[i][j]=dp[i-1][j-1]+1
#  (2) nums1[i-1]!=nums2[j-1]: dp[i][j]=max(dp[i-1][j], dp[i][j-1])
# 3. 初始化：dp[0][0]=0 dp[i][0]=0 dp[0][j]=0
# 4. 遍历顺序：从左到右 从上到下

# 时间复杂度：O(mn)
# 空间复杂度：O(mn)

class Solution(object):
    def maxUncrossedLines(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        dp=[[0]*(len(nums2)+1) for _ in range(len(nums1)+1)]
        for i in range(1, len(nums1)+1):
            for j in range(1, len(nums2)+1):
                if nums1[i-1]==nums2[j-1]:
                    dp[i][j]=dp[i-1][j-1]+1
                else:
                    dp[i][j]=max(dp[i-1][j], dp[i][j-1])
        return dp[-1][-1]
        