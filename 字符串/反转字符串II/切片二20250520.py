# 思路：每次遍历的时候，判断剩下的s的元素长度是否达到2k
# （1）如果不达到2k，则判断是否大于k
# （1.1）如果大于k，则反转前面的k个字符
# （1.2）如果小于k，则将这k个字符全部反转
# （2）如果达到2k，则反转前k个字符


class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        i=0
        chars=list(s)
        while i<len(chars):
            chars[i:i+k]=chars[i:i+k][::-1]
            i+=k*2
        return ''.join(chars)