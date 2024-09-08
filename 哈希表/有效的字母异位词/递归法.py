# 方法：递归法（也是哈希的一种用法）
# 时间复杂度：O(n+m+k)：n为s的长度；m为t的长度；k为memo的长度
# 空间复杂度：O(k)：字符集memo的大小

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        memo={} # 存储s字符串字符所出现的个数
        for i in s: # 依次记录字符出现的个数
            if i not in memo: # 未出现
                memo[i]=1
            else: # 出现过
                memo[i]+=1
        for i in t: # 对t的字符进行检查
            if i not in memo:  # 如果字符没有在memo中则直接返回false，因为相当于t中有字符不存在s中
                return False
            memo[i]-=1 # 如果出现则将它的次数直接减一
        for i in memo: # 对memo进行检查，如果全相同则memo的每个元素值都是0
            if memo[i]>0 or memo[i]<0:
                return False
        return True