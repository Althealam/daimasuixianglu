# 分析：如果s是由多个子串重复拼接而成的，那么多个s拼接在一起后，s一定会在其中
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        return s in (s+s)[1:-1]
        
        