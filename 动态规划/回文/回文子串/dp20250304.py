# 1. dp数组以及下标的含义：dp[i][j]表示区间范围[i,j]（左闭右闭）的子串是否是回文子串，如果是的话dp[i][j]为True，否则的话为False
# 2. 递推公式：
# （1）s[i]!=s[j]：dp[i][j]=False
# （2）s[i]==s[j]：
# （2.1）i==j：True
# （2.2）abs(i-j)==1：True
# （2.3）abs(i-j)>1：dp[i][j]=dp[i+1][j-1]
# 3. 初始化：dp[i][j]全部初始化为False
# 4. 遍历顺序：由递推公式可以知道dp[i][j]是由左下方推出来的，因此是从下到上，从左到右遍历

# 时间复杂度：O(n^2)
# 空间复杂度：O(n^2)

class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        dp=[[False]*len(s) for _ in range(len(s))]
        result=0 # 记录回文子串的数量
        for i in range(len(s)-1, -1, -1):
            for j in range(i, len(s)):
                if s[i]==s[j]:
                    if i==j:
                        dp[i][j]=True
                        result+=1
                    elif j-i==1:
                        dp[i][j]=True
                        result+=1
                    elif j-i>1:
                        dp[i][j]=dp[i+1][j-1]
                        if dp[i][j]:
                            result+=1
                elif s[i]!=s[j]:
                    dp[i][j]=False
        return result
            

