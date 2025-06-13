# 1. dp数组以及下标的含义：dp[i]表示偷窃到第i个房间时可以偷窃到的最高金额为dp[i]
# 2. 递推公式：
# （1）偷上一个房间：dp[i-1]
# （2）偷上上一个房间：dp[i-2]+num[i]
# dp[i]=max(dp[i-1]], dp[i-2]+num[i])
# 3. 初始化：dp[0]=num[0] dp[1]=max(num[0], num[1])
# 4. 遍历顺序：从左到右遍历

num = list(map(int, input().split()))

def ditui(num):
    if len(dp)==1:
        return dp[0]
    if len(dp)==0:
        return 0
    dp=[0]*len(num)
    dp[0]=num[0]
    dp[1]=max(num[0], num[1])
    for i in range(2, len(num)): # 遍历物品
        dp[i]=max(dp[i-2]+num[i], dp[i-1])
    return dp[-1]

result=ditui(num)
print(result)
