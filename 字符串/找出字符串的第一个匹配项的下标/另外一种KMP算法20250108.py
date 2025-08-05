# 思路：KMP算法
# 当出现字符串不匹配时，可以记录一部分之前已经匹配的文本内容，利用这些信息避免从头再去做匹配
# 前缀表：记录下表i之前（包括i）的字符串中，有多大长度的相同前缀后缀
# 求解next数组的思路：next[x]表示x（包括x）之前最长相等的前后缀长度

# 时间复杂度：O(m+n），其中m是文本串长度，n是模式串长度

class Solution(object):
    def getNext(self, next, s):
        next=[0] # 初始的值，此时没有公共的前后缀
        prefix_len=0 # 当前公共前后缀长度
        i=1 
        while i<len(s):
            if s[prefix_len]==s[i]:
                prefix_len+=1
                next.append(prefix_len)
                i+=1
            else:
                if prefix_len==0:
                    next.append(0)
                    i+=1
                else:
                    next.append(prefix_len-1)
        return next

    def strStr(self, haystack, needle):
        """
        :type haystack: str 文本串 主串
        :type needle: str 模式串 子串
        :rtype: int
        """
        if not needle:
            return 0
        next=[0]*len(needle)
        next=self.getNext(next,needle)
        j=-1
        for i in range(len(haystack)):
            while j>0 and haystack[i]!=needle[j+1]:
                j=next[j]
            if haystack[i]==needle[j+1]:
                j+=1
            if j==len(needle)-1:
                return i-len(needle)+1
        return -1
