class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        chars = list(s)
        for i in range(0, len(s), 2*k):
            chars[i:i+k] = self.reverse_list(chars[i:i+k])
        return ''.join(chars[:])
    
    def reverse_list(self, s):
        left, right = 0, len(s)-1
        while left<right:
            s[left], s[right] = s[right], s[left]
            left+=1
            right-=1
        return s