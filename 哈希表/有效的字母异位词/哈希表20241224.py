# 方法：哈希表
# 创建关于s的哈希表，统计每个字符的出现次数，再遍历t，减去相应的出现次数，最后判断是否全部为0
# 时间复杂度：O(n+m)
# 空间复杂度：O(1)


from collections import defaultdict
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        result=[0]*26
        for x in s:
            result[ord(x)-ord('a')]+=1
        for y in t:
            result[ord(y)-ord('a')]-=1
        for i in range(26):
            if result[i]!=0:
                return False
        return True 


