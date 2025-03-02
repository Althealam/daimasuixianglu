# 1. dp数组以及下标的含义：dp[i][j]表示以i-1为结尾的A和以下标j-1结尾的B，最长重复的子数组长度为dp[i][j]
# 2. 递推公式：如果A[i-1]==B[j-1]，那么dp[i][j]=dp[i-1][j-1]+1
# 3. 初始化：dp[i][0]和dp[0][j]没有意义，初始化为0 dp[0][0]=0
# 由于j=0和i=0都没有意义，因此需要初始化dp数组的长度为len(nums1)-1和len(nums2)-1
# 4. 遍历顺序：先遍历A再遍历B


# 时间复杂度：O(mn) 其中m是nums1的长度，n是nums2的长度
# 空间复杂度：O(mn)
class Solution(object):
    def findLength(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        dp=[[0]*(len(nums2)+1) for _ in range(len(nums1)+1)]
        result=0 # 记录最长公共子数组的长度
        for i in range(1, len(nums1)+1):
            for j in range(1, len(nums2)+1):
                if nums1[i-1]==nums2[j-1]:
                    dp[i][j]=dp[i-1][j-1]+1
                if dp[i][j]>result:
                    result=dp[i][j]
        return result