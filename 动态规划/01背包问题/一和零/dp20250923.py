# 1. dp数组以及下标的含义：dp[i][j]表示最多有i个0和j个1的strs的最大子集的大小为dp[i][j]
# 2. 递推公式：dp[i][j] = max(dp[i][j], dp[i-zeroNum][j-oneNum]+1)
# 3. 初始化：全部初始化为0
# 4. 遍历顺序：先物品后背包 背包逆序
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0]*(n+1) for _ in range(m+1)]
        for s in strs:
            zeroNum = s.count('0')
            oneNum = s.count('1')
            for i in range(m, zeroNum-1, -1):
                for j in range(n, oneNum-1, -1):
                    dp[i][j] = max(dp[i][j], dp[i-zeroNum][j-oneNum]+1)
        return dp[-1][-1]
        