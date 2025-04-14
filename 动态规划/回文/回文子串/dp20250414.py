# 1. dp数组以及下标的含义：dp[i][j]（一定要确保j>=i）表示下标为i到j的字符串是否是回文子串，如果是的话则为True，不是的话则为False
# 2. 递推公式：
# （1）s[i]!=s[j]:False
# （2）s[i]==s[j]：
# （2.1）i==j：True 比如a 将回文子串的数量
# （2.2）abs(i-j)=1：True 比如aa
# （2.3）abs(i-j)>1：dp[i][j]=dp[i+1][j-1]
# 3. 初始化：dp[i][j]全部初始化为False dp[0][0]=True
# 4. 遍历顺序：由递推公式可以知道dp[i][j]是由dp[i+1][j-1]推导出来的，因此遍历顺序是从下到上，从左到右（从左下角推导）

class Solution:
    def countSubstrings(self, s: str) -> int:
        dp=[[False]*len(s) for _ in range(len(s))]
        dp[0][0]=True
        result=0 # 计算回文子串的数量
        for i in range(len(s)-1, -1, -1):
            for j in range(i, len(s)):
                if s[i]!=s[j]:
                    dp[i][j]=False
                else:
                    if i==j or j-i==1:
                        result+=1
                        dp[i][j]=True
                    elif j-i>1 and dp[i+1][j-1]:
                        result+=1
                        dp[i][j]=dp[i+1][j-1]
        return result


        