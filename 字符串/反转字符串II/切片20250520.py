# 思路：每次遍历的时候，判断剩下的s的元素长度是否达到2k
# （1）如果不达到2k，则判断是否大于k
# （1.1）如果大于k，则反转前面的k个字符
# （1.2）如果小于k，则将这k个字符全部反转
# （2）如果达到2k，则反转前k个字符


class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        s=list(s)
        for i in range(0, len(s), 2*k):
            s[i:i+k]=self.reverse_substring(s[i:i+k])
        return ''.join(s)
    
    def reverse_substring(self, s):
        left=0
        right=len(s)-1
        while left<right:
            s[left], s[right]=s[right], s[left]
            left+=1
            right-=1
        return s


