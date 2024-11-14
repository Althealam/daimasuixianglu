# 分析：01背包

# 1. dp数组：dp[i][j]表示装i个0，j个1，最大有dp[i][j]个物品（需要求得结果dp[m][n]）
# 2. 递推公式：
# 纯01背包的递推公式：dp[i][j]=max(dp[i-1][j],dp[i-1][j-weight[i]]+value[i])
# 本题的递推公式：dp[i][j]=max(dp[i-x][j-y]+1,dp[i][j])（本题的value[i]=1）
# 3. 初始化：dp[0][0]=0   01背包的dp数组初始化为0即可
# 4. 遍历顺序：01背包一定是外层for循环遍历物品，内层for循环遍历背包容量且从后往前遍历

# 时间复杂度：
# 1. str列表的遍历：O(K*L)，其中K是字符串列表的长度，L是字符串的平均长度
# 2. 动态规划数组的更新：O(m*n)
# 总的时间复杂度：O(K*m*n)

# 空间复杂度：
# 1. 动态规划数组dp：O(m*n)
# 总的空间复杂度：O(m*n)

class Solution(object):
    
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        # 创建二维dp数组，初始化为0（m为1的数量，n为0的数量，并且m为行，n为列）
        dp=[[0]*(n+1) for _ in range(m+1)]

        for s in strs: # 遍历物品
            zeroNum=s.count('0') # 统计0的个数
            oneNum=len(s)-zeroNum # 统计1的个数
            for i in range(m,zeroNum-1,-1): # 遍历0的背包容量且从后向前遍历
                for j in range(n,oneNum-1,-1): # 遍历1的背包容量且从后向前遍历
                    dp[i][j]=max(dp[i][j],dp[i-zeroNum][j-oneNum]+1) # 状态转移方程
        return dp[m][n]
        