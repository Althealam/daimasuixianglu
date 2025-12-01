# 1. definition: dp[i] denotes when input is i-1, then the number of structurally unique BST's which has exactly n nodes of unique values from 1 to n
# 2. formula:
# let f[i, n] denotes the number of bst which have node i as the head and the number of nodes is n
# dp[i] = f[1]+f[2]+...+f[i]
# f[i, n] = dp[i-1]*dp[n-i] left tree have i-1 nodes and right tree have n-i nodes (i-1+n-1+1=n)
# dp[i] = dp[0]*dp[n]+dp[1]*dp[n-1]+...+dp[n-1]*dp[0]
# 3. initilization: dp[1]=1
# 4. order: i first, then j

class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0]*(n+1)
        dp[0]=1
        dp[1]=1
        for i in range(2, n+1): # the input which means the number of nodes in the bst is i
            for j in range(1, i+1): # the head
                dp[i]+=dp[j-1]*dp[i-j]
        return dp[-1]