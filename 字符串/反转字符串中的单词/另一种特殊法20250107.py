# 思路：删除空白+列表反转+单词反转
# 1. 时间复杂度：O(n)
# 2. 空间复杂度：O(n)
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        # 1. 反转整个列表
        s=s[::-1]
        # 2. 将字符串按照空格拆分为单词
        words=s.split()
        # 3. 反转单词
        s=' '.join(word[::-1] for word in words)
        return s