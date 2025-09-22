# 1. dp数组以及下标的含义：dp[i]表示输入为i，得到dp[i]种不同的二叉搜索树
# 2. 递推公式：dp[i]+=dp[j-1]*dp[i-j]
# 3. 初始化：dp[0]=1 dp[1]=1 dp[2]=2
# 4. 遍历顺序：从左到右

class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0]*(n+1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n+1):
            for j in range(1, i+1): # 头节点
                dp[i]+=dp[j-1]*dp[i-j]
        return dp[-1]
        