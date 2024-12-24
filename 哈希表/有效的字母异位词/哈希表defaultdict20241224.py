# 方法：哈希表defaultdict
# 思路：创建关于s和t的两个哈希表，判断两个哈希表是否相同即可

# 时间复杂度：O(m+n)
# 空间复杂度：O(m+n)（需要创建两个字典来存储出现的次数）

from collections import defaultdict
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_dict=defaultdict(int)
        t_dict=defaultdict(int)
        for x in s:
            s_dict[x]+=1
        for x in t:
            t_dict[x]+=1
        return s_dict==t_dict


