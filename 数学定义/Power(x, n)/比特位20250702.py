# 时间复杂度：O(logn)
# 空间复杂度：O(1)
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x==0 or x==1:
            return x
        if n<0:
            n=-n
            x = 1/x
        while n: # 从低到高枚举n的每个比特位
            if n&1: # 当前的比特位为1
                ans*=x # 将x乘以到ans中
            x*=x # x自身平方
            n>>=1 # 继续枚举下一个比特位
        return ans

