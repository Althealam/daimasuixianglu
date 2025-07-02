# 时间复杂度：O(n)，因为n!中因子5的个数为O(n)
# 空间复杂度：O(1)
# 如果是单纯的计算n!然后求出0的数量，会导致时间复杂度非常的高
class Solution:
    def trailingZeroes(self, n: int) -> int:
        ans = 0
        for i in range(5, n+1, 5):
            while i%5==0:
                i//5
                ans+=1
        return ans
        