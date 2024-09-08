# 哈希表的数据结构：数组（hash值比较小并且范围也比较小）、set、map
# 思路：遇到哈希时，先考虑使用数组
# 分析：由于这个题只会出现小写字母，因此可以ASCII码对应0-25（26个字符）
# 用哈希表存储s中每个字符出现的次数，减去t中每个字符出现的次数
# 如果哈希表最后的每个元素都是0，就说明符合题目条件
# 在遍历字符串s的时候，只需要将s[i]-'a'所在的元素做+1即可，并不需要记住字符a的ASCII，只要求出一个相对数值即可

# 时间复杂度：O(n)，其中n是字符串s和t的长度之和，因为每个字符串都要遍历一次
# 空间复杂度：O(1) 定义一个常量大小的辅助数组，不随着输入字符串的长度变化

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        record=[0]*26 # 创建一个用于记录的数组
        for i in s:
            record[ord(i)-ord('a')]+=1
            # ord是python的一个内置函数，用于将一个字符转换成其对应的ASCII码
            # ASCII是一种字符编码标准，用于将英文字符和其他一些特殊符号表示为数字
            # ord(i)：获取字符串s中每个字符的ASCII码
            # ord(i)-ord('a')：计算出每个字符相对于a的偏移量
            # 由于题目只涉及到小写字符，所以偏移量的范围是0-25，正好对应一个长度为26的数组
            # Eg：如果i为a，那么就是record[0]+=1；如果i为b，就是record[1]+=1（记录每个小写字符出现的次数）

        for i in t:
            record[ord(i)-ord('a')]-=1
        for i in range(26):
            if record[i]!=0:
                # record数组如果有的元素不为0，说明s和t一定是谁多了字符或者谁少了字符
                return False
        return True