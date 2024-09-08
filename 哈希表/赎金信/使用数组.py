# 方法一：使用数组

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
        ransom_count=[0]*26
        magazine_count=[0]*26
        for c in ransomNote:
            ransom_count[ord(c)-ord('a')]+=1
        for c in magazine:
            magazine_count[ord(c)-ord('a')]+=1
            # ord用于将一个字符串转换为对应的ASCII码值
        return all(ransom_count[i]<=magazine_count[i] for i in range(26))
        # all用于检查可迭代对象中的所有元素是否都满足某个条件
        # i遍历从0到25，对应英文字母a到z
        # 对于每个i，ransomNote中的字符计数ransom_count[i]是否小于等于magazine_count[i]