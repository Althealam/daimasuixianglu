# 思路：二分法，找到mid*mid<=x的地方，直到left和right重合（x的平方根一定在[0, x]之间）
# 时间复杂度：O(logx)，每次迭代将搜索区间的长度减半，直到区间为空，因此迭代次数为logx
# 空间复杂度：O(1)
class Solution:
    def mySqrt(self, x: int) -> int:
        left, right, ans = 0, x, -1
        while left<=right: # 闭区间[left, right]
            mid = (left+right)//2
            if mid*mid<=x:  # [mid+1, right]
                ans = mid
                left = mid+1
            else: # [left, mid-1]
                right = mid-1
        return ans

        