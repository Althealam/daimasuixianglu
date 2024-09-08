# 方法二：双指针法
# 思路：先将完整的字符串进行反转，然后再对字符串内空格分开的小字符串进行反转
# 定义快指针用于获取符合题目要求的字母
# 定义慢指针，获取到符合要求的字母后更新的位置

# 时间复杂度：O(n)
# 空间复杂度：O(n)
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        # 将字符串拆分为单词，即转换为列表类型
        words=s.split()

        # 反转单词
        left,right=0,len(words)-1
        while left<right:
            words[left],words[right]=words[right],words[left]
            left+=1
            right-=1
        
        # 将列表转换为字符串
        return " ".join(words)