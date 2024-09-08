# 方法三：使用count
# 时间复杂度：O(m+n)，m是ransomNote的长度，n是magazine的长度
# 空间复杂度：O(1)，每个数组都是固定的常数空间
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        for char in ransomNote:
            if char in magazine and ransomNote.count(char)<=magazine.count(char):
                continue
            else:
                return False
        return True