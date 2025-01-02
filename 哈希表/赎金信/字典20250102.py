# 思路：构建一个hash表来统计magazine里面的字符出现的次数，然后遍历ransom，减去ransom的各个字母出现的次数
# 最后，判断hash的每个元素是否都是大于等于0的

# 时间复杂度：O(m+n)，m是magazine的长度，n是ransomNote的长度
# 空间复杂度：O(1)
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        hash=[0]*26
        for text_m in magazine:
            hash[ord(text_m)-ord('a')]+=1
        for item_r in ransomNote:
            hash[ord(item_r)-ord('a')]-=1
            if hash[ord(item_r)-ord('a')]<0:
                return False
        return True