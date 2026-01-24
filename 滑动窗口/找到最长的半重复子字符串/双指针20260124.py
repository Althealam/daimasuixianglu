# 统计连续出现的子字符串的数量
class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        left = 0
        max_length = 0
        count = 0 # 连续出现的子字符串的数量
        for right, c in enumerate(s):
            # 需要增加的情况
            if right>0 and s[right]==s[right-1]:
                count+=1
            
            # 滑动窗口移动指针的情况
            while count>1: # 如果出现了不止一组连续的子字符串
                if s[left]==s[left+1]:
                    count-=1
                left+=1
            max_length = max(max_length, right-left+1)
        return max_length


            
