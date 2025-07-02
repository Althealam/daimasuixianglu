class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res = 0
        for i in range(len(digits)-1, -1, -1):
            res += digits[i]*(10**(len(digits)-i-1))
        ans = []
        for item in str(res+1):
            ans.append(int(item))
        return ans