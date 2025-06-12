# 1. dp数组以及下标的含义：dp[j]表示爬到第j个台阶有dp[j]种方法
# 2. 递推公式：dp[j]+=dp[j-i] i从1到m遍历
# 3. 初始化：dp[0]=1
# 4. 遍历顺序：本题是求排列数，因此是先背包后物品
n, m = map(int, input().split())

def ditui(n, m):
    dp=[0]*(n+1)
    dp[0]=1

    for j in range(1, n+1): # 遍历背包
        for i in range(1, m+1): # 遍历物品
            if j>=i:
                dp[j]+=dp[j-i]
    return dp[-1]

result=ditui(n, m)
print(result)
