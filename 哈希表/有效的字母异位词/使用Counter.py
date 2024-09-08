# 方法：使用Counter
# Counter是一个字典子类，用于计数可哈希对象，它通常用来统计元素出现的次数
# 时间复杂度：O(n)，n是s和t的长度之和
# 空间复杂度：O(1)，Counter对象的大小取决于字符集的大小，而不是字符串的长度
# 在这个问题中，字符集大小是固定的，也就是小写字母的数量

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        from collections import Counter
        a_count=Counter(s)
        b_count=Counter(t)
        return a_count==b_count