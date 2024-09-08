# 方法一：使用字典

# 思路：求解字符串a能不能组成字符串b，不用管字符串b能不能组成字符串a，利用空间换时间的策略来解题
# magazine：包含 ransomNote：被包含

# 方法：用一个长度为26的数组来记录magazine里字母出现的次数
# 然后再用ransomNote去验证这个数组是否包含了ransomNote所需要的所有字母

# 注意：1. 杂志里面的字母不能重复使用
#      2. 只有小写字母

# 时间复杂度：O(m+n)，m是ransomNote的长度，n是magazine的长度
# 空间复杂度：O(1)，每个数组都是固定的常数空间
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        counts={}
        for c in magazine:
            counts[c]=counts.get(c,0)+1
            # 检查是否已经有该字符的计数，如果有就增加1，如果没有就设置为1
        for c in ransomNote:
            if c not in counts or counts[c]==0:
                return False
            counts[c]-=1 # 表示已经使用了一个该字符（注意！！！）
        return True