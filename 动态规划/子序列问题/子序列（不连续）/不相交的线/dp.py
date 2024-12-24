# 分析：相当于是找相同的子序列，并且需要保证顺序相同（本题就是求最长的公共子序列）
# 1. dp数组：dp[i][j]表示的是长度为[0,i-1]的字符串text1与长度为[0,j-1]的字符串text2的最长公共子序列为dp[i][k]
# 2. 递推公式：
# if text1[i-1]==text2[j-1]: dp[i][j]=dp[i-1][j-1]+1
# else: dp[i][j]=max(dp[i-1][j],dp[i][j-1])
# 3. 初始化：
# dp[i][0]=0 dp[0][j]=0
# 4. 遍历顺序：从左到右 从上到下
class Solution(object):
    def maxUncrossedLines(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        dp=[[0]*(len(nums2)+1) for _ in range(len(nums1)+1)]
        for i in range(1,len(nums1)+1):
            for j in range(1,len(nums2)+1):
                if nums1[i-1]==nums2[j-1]:
                    dp[i][j]=dp[i-1][j-1]+1
                else:
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1])
        return dp[len(nums1)][len(nums2)]
        