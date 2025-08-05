# 暴力法：
# 1. 外层循环遍历haystack中所有可能的起始位置
# 2. 内层循环从i开始，逐个比对haystack和needle的字符
# 如果所有字符都匹配，则返回当前起始索引
# 如果发现不匹配的字符，则跳出循环
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # 两种特殊情况：一是needle不存在，二是needle比haystack要长
        if not needle:
            return -1
        if len(needle)>len(haystack):
            return -1

        for i in range(len(haystack)-len(needle)+1): # 这里减去needle是因为尾部要留有足够空间的字符串
            match = True
            for j in range(len(needle)):
                if haystack[i+j]!=needle[j]:
                    match = False
                    break
            if match:
                return i
        return -1


        