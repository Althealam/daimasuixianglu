# 1. dp数组以及下标的含义：dp[i]表示爬到第i个台阶，有dp[i]种方法
# 2. 递推公式：
# （1）从下一个台阶爬上来有dp[i-1]种方法
# （2）从下两个台阶爬上来有dp[i-2]种方法
# （3）从下三个台阶爬上来有dp[i-3]种方法
# 总结：dp[i]+=dp[i-j]
# 背包是总的台阶数n，物品是每次爬的台阶数
# 3. 初始化：dp[0]=1
# 4. 遍历顺序：本题是求排列数，因此先背包，后物品



n, m=map(int, input().split())
# n表示需要n阶台阶，m表示最多爬m个台阶

def palouti(n, m):
    dp=[0]*(n+1)
    dp[0]=1

    for j in range(1, n+1): # 遍历背包
        for i in range(1, m+1): # 遍历物品
            if j>=i:
                dp[j]+=dp[j-i] 
    return dp[n]

result=palouti(n, m)
print(result)