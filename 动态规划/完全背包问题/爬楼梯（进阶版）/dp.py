# 完全背包问题
# 1阶、2阶、3阶就是物品（每一阶可以重复使用）
# 楼顶就是背包

# 1. dp数组的含义：dp[i]表示爬到有i个台阶的楼顶，有dp[i]种方法
# 2. 确定递推公式：dp[i]+=dp[i-j]
# 3. dp数组的初始化：
# 由于dp[i]+=dp[i-j]，因此dp[0]=1（dp[0]是递归中一切数值的基础，如果dp[0]=0的化，其他数值也都是0）
# 4. 确定遍历顺序：本题是背包求排列问题，需要将背包放在外循环，物品放在内循环
# 也就是target放在外循环，nums放在内循环

def climbing_stairs(n,m):
    # n是台阶总数，也就是target
    # m是每次可以最多爬几个台阶
    dp=[0]*(n+1) # 背包总容量
    dp[0]=1 # 初始化
    # 排列题，背包在外，物品在内
    for j in range(1,n+1): # 背包 
        for i in range(1,m+1): # 物品
            if j>=i: # 先遍历背包，后遍历物品时，需要检查背包容量是否可以容纳物品
                dp[j]+=dp[j-i]
    return dp[n]
    
if __name__='__main__':
    n,m=list(map(int,input().split(' ')))
    print(climbing_stairs(n,m))
                