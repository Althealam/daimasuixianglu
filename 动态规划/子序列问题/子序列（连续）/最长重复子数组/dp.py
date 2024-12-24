# 动态规划五部曲
# 1. dp数组：dp[i][j]表示的是以i-1为结尾的nums1和以j-1结尾的nums2的最长公共子数组长度
# 2. 递推公式：
# if nums[i-1]==nums[j-1]: dp[i][j]=dp[i-1][j-1]+1
# 3. 初始化：
# dp[i][0]和dp[0][j]没有意义，应该初始化为0，将dp数组其他的初始化为0
# 4. 遍历顺序：遍历nums1和nums2，先遍历哪个数组是没关系的

# 时间复杂度：O(n^2)
# 空间复杂度：O(n^2)

class Solution(object):
    def findLength(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        # dp[i][j]表示的是以i-1为结尾的nums1和以j-1结尾的nums2的最长公共子数组的长度
        # i表示行，j表示列
        dp=[[0]*(len(nums2)+1) for _ in range(len(nums1)+1)]
        # 记录最长公共子数组的长度
        result=0

        # 遍历数组nums1
        for i in range(1,len(nums1)+1):
            # 遍历数组nums2
            for j in range(1,len(nums2)+1):
                if nums1[i-1]==nums2[j-1]:
                    dp[i][j]=dp[i-1][j-1]+1
                if dp[i][j]>result:
                    result=dp[i][j]

        return result

        