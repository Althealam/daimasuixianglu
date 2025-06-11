# 1. dp数组以及下标的含义：dp[i][j]表示有i个0和j个1的strs的最大子集的大小为dp[i][j]
# 2. 递推公式：
# （1）不放入物品：dp[i][j]
# （2）放入物品：dp[i-zeroNum[j-oneNum]+1 其中zeroNum和oneNum为当前物品的1和0的数量
# dp[i][j]=max(dp[i][j], dp[i-zeroNum][j-oneNum]+1)
# 3. 初始化：全部初始化为0
# 4. 遍历顺序：先物品后背包，背包逆序（本题目的i和j也是背包容量，所以这道题应该是一个一维数组）

strs=list(map(str, input().split()))
m=int(input()) # 0的数量
n=int(input()) # 1的数量

def ditui(strs, m, n):
    dp=[[0]*(n+1) for _ in range(m+1)] # m行n列，m个0和n个1
    for str in strs: # 遍历物品
        oneNum=str.count('1') # 当前物品的1的数量
        zeroNum=str.count('0') # 当前物品的0的数量
        # 遍历背包
        for i in range(m, zeroNum-1, -1):  # 遍历0的数量
            for j in range(n, oneNum-1, -1): # 遍历1的数量
                dp[i][j]=max(dp[i][j], dp[i-zeroNum][j-oneNum]+1)
    return dp[m][n]


result=ditui(strs, m, n)
print(result)