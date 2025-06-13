# 1. dp数组以及下标的含义：dp[i]表示字符串长度为i的话，如果dp[i]为True，表示可以拆分为一个或者多个在字典中出现的词
# 2. 递推公式：
# 如果dp[j]为True，并且[j, i]的子串出现在字典里，那么dp[i]也为True
# 3. 初始化：全部初始化为False dp[0]=True
# 4. 遍历顺序：本题是完全背包，并且是排列数，因此是先背包后物品（组合数为先物品后背包）

s=str(input()) # 背包
wordDict=list(map(str, input().split())) # 物品
# 判断s是否能用wordDict中的物品装满

def ditui(s, wordDict):
    wordSet=set(wordDict)
    dp=[False]*(len(s)+1)
    dp[0]=True

    for i in range(1, len(s)+1): # 遍历背包
        for j in range(i): # 遍历物品
            if dp[j] and s[j:i] in wordSet:
                dp[i]=True
                break
    return dp[-1]

result=ditui(s, wordDict)
print(result)
