# 1. dp数组以及下标的含义：dp[i][j]表示最多有i个0和j个1的strs的最大子集的大小为dp[i][j]
# 2. 递推公式：dp[i][j]可以由前一个strs里的字符串推导出来，strs里的字符串有zeroNum个0，oneNum个1
# dp[i][j]=max(dp[i][j], dp[i-zeroNum][j-oneNum]+1)
# 3. 初始化：全部初始化为0
# 4. 遍历顺序：由于本题的dp数组没有涉及到背包，都是物品，因此其实可以看作为一维dp数组
# 本题的物品时strs中的字符串，背包容量就是题目描述中的m和n
# 先物品，后背包，并且背包要逆序遍历

class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp=[[0]*(n+1) for _ in range(m+1)]
        for s in strs: # 遍历物品
            zeroNum=s.count('0') # 0的个数
            oneNum=s.count('1') # 1的个数
            for i in range(m, zeroNum-1, -1):
                for j in range(n, oneNum-1, -1):
                    dp[i][j]=max(dp[i][j], dp[i-zeroNum][j-oneNum]+1)
        return dp[m][n]


        