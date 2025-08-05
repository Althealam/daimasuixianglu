# 思路：KMP算法
# KMP算法适用于匹配模式串是否存在于文本串中的问题（暴力匹配的时间复杂度为O(m*n)，其中m为文本串的长度，n为模式串的长度）
# 前缀：除了最后一个字符外，字符串的所有的头部子串（由第一个字符开始排列）
# 后缀：除了第一个字符外，字符串的所有的尾部子串（由最后一个字符开始排列）
# 部分匹配值：字符串的前缀和后缀的最大公共前后缀长度

class Solution(object):
    def getNext(self,next,s):
        # self：在类的方法中使用，表示类的实例
        # next：数组，用于存储计算结果
        # s：模式字符串（在文本中搜索的字符串）
        j=-1 # j用于跟踪模式字符串中当前比较的字符的位置
        next[0]=j
        for i in range(1,len(s)): # 遍历模式字符串s的每个字符，从第二个字符开始，直到字符串的末尾
            while j>=0 and s[i]!=s[j+1]: # 检查当前字符s[i]是否与j位置之后的字符s[j+1]相同
            # 如果j是-1或者字符不匹配，循环继续
                j=next[j] # 将next数组的当前索引i处的值设置为j
                # 这个值表示在当前位置之前，模式字符串中最长相等的前缀和后缀的长度
            if s[i]==s[j+1]:
                j+=1
            next[i]=j

    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0
        next=[0]*len(needle)
        self.getNext(next,needle)
        j=-1
        for i in range(len(haystack)):
            while j>=0 and haystack[i]!=needle[j+1]:
                j=next[j]
            if haystack[i]==needle[j+1]:
                j+=1
            if j==len(needle)-1:
                return i-len(needle)+1
        return -1