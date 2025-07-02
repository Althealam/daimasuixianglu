# 思路：分治
# 1. 在计算power(x, n)时，先递归计算出y==x**(n//2)，其中n//2向下取整
# 2. 根据递归计算的结果，如果n为偶数，那么power(x, n)为y**2；如果n为奇数，那么power(x, n)=y**2 * x
# 3. 递归的边界条件为n=0，任意数的0次方都是1

# 时间复杂度：O(logn)，也就是递归的层数
# 空间复杂度：O(logn)，也是递归的层数，因为递归的时候会使用栈空间

# power(x, 64) = x->power(x, 2)->power(x, 4)->power(x, 8)->power(x, 16)->power(x, 32)->power(x, 64)
# power(x, 77) = x->power(x, 2)->power(x, 4)->power(x, 9)->power(x, 19)->power(x, 38)->power(x, 77)

class Solution:
    def myPow(self, x: float, n: int) -> float:
        def quickMul(N):
            if N==0:
                return 1.0
            y = quickMul(N//2)
            return y*y if N%2==0 else y*y*x
        
        return quickMul(n) if n>=0 else 1.0/quickMul(-n)

