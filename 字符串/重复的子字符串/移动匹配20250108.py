# 思路：如果某个字符串是由多个子串重复构成的，假设这个字符串是s
# 那么可以知道s+s中一定可以找到s，注意需要提出s+s的前后两个元素

# 时间复杂度：O(n^2)
# 1. 构造new_s：字符串拼接操作的时间复杂度和参与拼接的字符串长度有关
# 2. 判断子串是否存在：最坏的情况下时间复杂度是O(nx(2n-2))=O(n^2)
# 空间复杂度：O(n)（构造了一个长度为2n的字符串，因此会占用额外的空间）

class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        new_s=s+s
        if s in new_s[1:-1]:
            return True
        return False
        