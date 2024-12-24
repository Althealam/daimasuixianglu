# 回文子串就是从中间开始左右两边是对称的
# 1. dp数组的含义：dp[i][j]表示的是s的i到j的范围内是否是一个回文串，如果是的话，向两边拓展的时候，只需要判断s[i:j]左右两边的元素是否相同
# 2. 递推公式：
# if s[i]==s[j]: 
# (1)i==j: True（同一个字符，例如a，这时候是回文子串）
# (2)i-j=1: True（相差为1，例如aa，这时候也是回文子串）
# (3)i-j>1: 判断dp[i+1][j-1]，如果dp[i+1][j-1]==True, 那么dp[i][j]=True
# （例如cabac, 此时的s[i]和s[j]已经相同了，看到i到j区间是不是回文子串就看aba是不是回文，那么aba的区间就是i+1与j-1区间）
# else的时候s[i]!=s[j]，默认为False了，因此不用讨论
# 3. 初始化：dp[i][j]=False
# 4. 遍历顺序：dp[i][j]依赖于dp[i+1][j-1]，因此遍历顺序为从下到上，从左到右

# 用result来记录回文子串的数量
# 时间复杂度：O(n^2)
# 空间复杂度：O(n^2)

class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        dp=[[False]*len(s) for _ in range(len(s))]
        result=0
        for i in range(len(s)-1,-1,-1): # 从下到上
            for j in range(i,len(s)): # 从左到右
                if s[i]==s[j]:
                    if j-i<=1: # 情况1和情况2
                        result+=1
                        dp[i][j]=True
                    elif j-i>1:
                        if dp[i+1][j-1]==True:
                            result+=1
                            dp[i][j]=True
        return result
        