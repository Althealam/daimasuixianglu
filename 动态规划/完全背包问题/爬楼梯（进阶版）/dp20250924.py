# 1. dp数组以及下标的含义：dp[i]表示爬到第i个台阶，有dp[i]种方法
# 2. 递推公式
# dp[i]+=dp[i-j]
# 3. 初始化：dp[0]=1
# 4. 遍历顺序：排列数，先背包后物品

n, m = map(int, input().split())

def palouti(n, m):
    dp=[0]*(n+1)
    dp[0] = 1
    for j in range(1, n+1): # 遍历背包
        for i in range(1, m+1): # 遍历物品
            dp[j]+=dp[j-i]
    return dp[n]

result = palouti(n, m)
print(result)
