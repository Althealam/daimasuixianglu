# 1. dp数组以及下标的含义：dp[j][j]表示以nums1[i-1]为结尾的A，和以nums2[j-1]为结尾的B，其最长重复子数组的长度为dp[i][j]
# 2. 递推公式：
# if nums1[i-1]==nums2[j-1]: dp[i][j]=dp[i-1][j-1]+1
# 3. 初始化：全部初始化为0 dp[i][0]=0 dp[0][j]=0（因为dp[i][j]都是从dp[i][0]和dp[0][j]推导出来的）
# 4. 遍历顺序：从前向后遍历
class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        dp=[[0]*(len(nums2)+1) for _ in range(len(nums1)+1)]
        result=0 # 记录最长重复子数组的长度
        for i in range(1, len(nums1)+1):
            for j in range(1, len(nums2)+1):
                if nums1[i-1]==nums2[j-1]:
                    dp[i][j]=dp[i-1][j-1]+1
                if dp[i][j]>result:
                    result=dp[i][j]
        
        return result
        