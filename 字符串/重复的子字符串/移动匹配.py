# 方法：移动匹配
#思路：假设原来的字符串为s，拼接s与s，并且删除首字母与尾字母（避免在s+s中搜索出原来的s），判断s+s中是否还有出现s，如果有的话s就是由重复的子字符串构成的
# 时间复杂度：O(n^2)，主要由字符串查找操作决定
# 空间复杂度：O(n)，主要由存储新字符串ss所需要的空间决定
class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n=len(s)
        if n<=1: # 如果n<=1的时候，讨论是否由重复的子串构成是没有意义的
            return False
        ss=s[1:]+s[:-1]
        # s[1:]：字符串s去掉第一个字符后的部分
        # s[:-1]：字符串s去掉最后一个字符前的部分
        print(ss.find(s)) # 打印新字符串ss中第一次出现原字符串s的索引
        # 如果s可以在ss中找到，说明s是由重复的子串构成的
        return ss.find(s)!=-1