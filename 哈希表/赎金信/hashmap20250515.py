# 思路：
# 1. 定义hashmap1，统计magazine中每个字符的出现次数
# 2. 定义hashmap2，统计ransomNote中每个字符的出现次数
# 3. 判断hashmap2的每个值是否小于等于hashmap1
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hashmap=[0]*26
        for i in magazine:
            hashmap[ord(i)-ord('a')]+=1
        
        for i in ransomNote:
            hashmap[ord(i)-ord('a')]-=1
            if hashmap[ord(i)-ord('a')]<0:
                return False

        return True

        
        