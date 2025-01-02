# 思路：构建一个hash表来统计magazine里面的字符出现的次数
# 遍历ransomNote，查找ransomNote中的item是否在hash中出现，如果没有直接返回false，如果有的话则减去对应的次数

# 时间复杂度：O(m+n)
# 空间复杂度：O(m)，hashdict统计magazine字符串中出现的字符以及出现的次数

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        from collections import defaultdict
        hashdict=defaultdict(int)
        for item in magazine:
            if item not in hashdict.keys():
                hashdict[item]=1
            else:
                hashdict[item]+=1
        for item in ransomNote:
            value=hashdict[item]
            if not value:
                return False
            else:
                hashdict[item]-=1
        return True
