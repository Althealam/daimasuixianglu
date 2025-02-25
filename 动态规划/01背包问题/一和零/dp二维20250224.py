# 1. dp数组及其下标的含义：dp[i][j]表示最多有i个0和j个1的strs的最大子集的大小为dp[i][j]
# 2. 递推公式：假设前一个dp[i][j]中0的数量是zero_num，1的数量是one_num
# dp[i][j]=max(dp[i][j],dp[i-zero_num][j-one_num]+1)
# （1）不包含这个str：dp[i][j]
# （2）包含这个str：dp[i-zero_num][j-one_num]+1
# 3. 初始化：m+1行n+1列，m是0的数量，n是1的数量
# 4. 遍历顺序：外层为物品，内层为背包，并且背包的遍历是逆序

# 时间复杂度：O(kxmxn)，其中k是字符串列表strs的长度，m和n分别是0和1的最大可用数量
# 空间复杂度：O(mxn)

class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        dp=[[0]*(n+1) for _ in range(m+1)]
        for s in strs: # 遍历物品
            zeroNum=s.count('0') # 统计0的个数
            oneNum=s.count('1') # 统计1的个数
            for i in range(m, zeroNum-1, -1): # 遍历背包zeroNum
                for j in range(n, oneNum-1, -1): # 遍历背包oneNum
                    dp[i][j]=max(dp[i][j], dp[i-zeroNum][j-oneNum]+1)
        return dp[m][n]
        