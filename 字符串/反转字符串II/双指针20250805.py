class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        i = 0
        chars = list(s)
        while i<len(chars):
            chars[i:i+k] = self.reverse_string(chars[i:i+k])
            i+=2*k
        return ''.join(chars)

    
    def reverse_string(self, s):
        left, right = 0, len(s)-1
        while left<=right:
            s[left], s[right] = s[right], s[left]
            left+=1
            right-=1
        return s