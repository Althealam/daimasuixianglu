# 时间复杂度：O(nlogn)
# 利用sorted函数进行排序，排序算法的时间复杂度为O(nlogn)
# 空间复杂度：O(n)
# sorted函数对字符串进行排序时，会创建新的排序后的字符串对象，因此需要额外的空间
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if sorted(s)==sorted(t):
            return True
        return False
