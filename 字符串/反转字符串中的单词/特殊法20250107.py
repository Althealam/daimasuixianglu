# 思路：拆分字符串+反转列表
# 1. 时间复杂度：O(n)
# 2. 空间复杂度：O(n)
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        # 1. 将字符串按照空格拆分为单词
        words=s.split() 
        # 2. 反转单词
        words=words[::-1]
        return ' '.join(words) 