# 方法：KMP算法
# 如果在一个串中查找另外一个串是否出现过，那么就是KMP算法的主场
# 思路：如果字符串s是由重复子串组成的，那么最长相等前后缀不包含的子串就是字符串s的最小重复子串

class Solution(object):
    def getNext(self, next, s):
        j=0
        for i in range(1,len(s)):
            while j>0 and s[i]!=s[j]: # 无法匹配
                j=next[j-1]
            if s[i]==s[j]: # 成功匹配
                j+=1
            next[i]=j
        return next

    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        next=[0]*len(s)
        next=self.getNext(next,s)
        if next[-1]!=0 and len(s)%(len(s)-next[-1])==0:
            return True
        return False

        