# 思路
# 1. 定义反转固定字符串的函数reverse_substring
# 2. 将s[cur:cur+k]进行反转，并且cur每次都走2k步

# 时间复杂度：O(n)
# 空间复杂度：O(n)，n表示输入字符串s的长度
class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        def reverse_substring(text):
            """
            给定text，返回反转后的text
            """
            left=0
            right=len(text)-1
            while left<=right:
                text[left],text[right]=text[right],text[left]
                left+=1
                right-=1            
            return text
        result=list(s)
        # 遍历每个2*k的区间，然后反转固定的i:i+k的字符串
        for i in range(0,len(result),2*k):
            result[i:i+k]=reverse_substring(result[i:i+k])
        return ''.join(result)
        # ''表示连接时使用的分隔符
        # 意味着将可迭代对象result中的元素依次拼接放在一起
        

        