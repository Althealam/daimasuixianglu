# 1. dp数组以及下标的含义：dp[i][j]表示[i,j]的字符串是否是回文子串，如果是的话则为True，否则的话为False
# 2. 递推公式：
# （1）s[i]==s[j]
# （1.1）dp[i][j]=dp[i+1][j-1]（j-1-i-1>=0==>j-i>=2==>j-i>1，需要讨论j-i<=1的情况）
# （1.2）i==j：True
# （1.3）j-i=1: True
# （2）s[i]!=s[j]: False
# 3. 初始化：全部初始化为False dp[0][0]=True
# 4. 遍历顺序：先遍历j，再遍历i 从下到上 从左到右
s = str(input())

def ditui(s):
    dp=[[False]*len(s) for _ in range(len(s))]
    dp[0][0]=True
    result=0 # 回文子串的数量
    for i in range(len(s)-1, -1, -1): # 从下到上
        for j in range(i, len(s)): # 从左到右
            if s[i]==s[j]:
                if i==j:
                    dp[i][j]=True
                elif j-i==1:
                    dp[i][j]=True
                else:
                    dp[i][j]=dp[i+1][j-1]
            else:
                dp[i][j]=False

            if dp[i][j]:
                result+=1
    return result

result=ditui(s)
print(result)