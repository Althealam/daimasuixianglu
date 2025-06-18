# 1. dp数组以及下标的含义：dp[i][j]表示以text1[i-1]为结尾和以text2[j-1]为结尾的最长公共子序列的长度
# 2. 递推公式：
# （1）text1[i-1]==text2[j-1]: dp[i][j]=dp[i-1][j-1]+1
# （2）text1[i-1]!=text2[j-1]: dp[i][j]=max(dp[i-1][j], dp[i][j-1])
# 3. 初始化：全部初始化为0
# 4. 遍历顺序：先遍历text1再遍历text2
text1 = str(input())
text2 = str(input())


def ditui(text1, text2):
    dp=[[0]*(len(text2)+1) for _ in range(len(text1)+1)]
    result=0
    for i in range(1, len(text1)+1):
        for j in range(1, len(text2)+1):
            if text1[i-1]==text2[j-1]:
                dp[i][j]=dp[i-1][j-1]+1
            else:
                dp[i][j]=max(dp[i-1][j], dp[i][j-1])
            result=max(result, dp[i][j])
    return result

result=ditui(text1, text2)
print(result)
