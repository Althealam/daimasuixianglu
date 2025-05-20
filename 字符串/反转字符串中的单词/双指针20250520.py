class Solution:
    def reverseWords(self, s: str) -> str:
        chars=s.split(' ')
        res=[]
        for char in chars:
            if char!="":
                res.append(char)
        left=0
        right=len(res)-1
        while left<right:
            res[left], res[right]=res[right], res[left]
            right-=1
            left+=1
        return ' '.join(res)