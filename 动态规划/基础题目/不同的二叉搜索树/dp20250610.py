# 1. dp数组以及下标的含义：dp[i]表示以1, .., i为节点组成的二叉搜索树有dp[i]种
# 2. 递推公式：
# dp[i]=f(1)+f(2)+...+f(i)，其中f(j)表示以j为根节点的二叉搜索树有f(j)种
# 其中f(j)=dp[j-1]*dp[i-j]，表示左子树有dp[j-1]种，右子树有dp[i-j]种，总共有i个节点
# 因此：dp[i]+=dp[j-1]*dp[i-j]，其中j从1到i
# 3. 初始化：dp[0]=1 dp[1]=1
# 4. 遍历顺序：从前向后遍历

n=int(input())

def ditui(n):
    dp=[0]*(n+1)
    dp[0]=1
    dp[1]=1
    for i in range(2, n+1):
        for j in range(1, i+1):
            dp[i]+=dp[j-1]*dp[i-j]
    return dp[n]