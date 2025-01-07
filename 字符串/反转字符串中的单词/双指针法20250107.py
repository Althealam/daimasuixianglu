# 思路：
# 1. 将s按照空格拆分为单词
# 2. 反转单词
# 3. 将单词列表用空格拼接起来
# 时间复杂度：O(n)
# (1)split操作将字符串按照空格分割，需要遍历整个字符串
# (2)反转单词需要进行m/2次，其中m是单词的数量
# (3)join操作的时间复杂度是O(m)
# 空间复杂度：O(n)
# (1)split操作会创建一个新的列表来存储分割后的单词，因此需要O(n)
# (2)join操作会有一些临时的空间开销用于拼接等操作
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        # 1. 将字符串按照空格拆分为单词
        words=s.split() 
        # 2. 反转单词
        left=0
        right=len(words)-1
        while left<=right:
            words[left],words[right]=words[right],words[left]
            left+=1
            right-=1
        return " ".join(words)
        
        
        