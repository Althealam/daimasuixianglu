# 分析：贝祖定理
# 目标位找到一对整数a和b，使得ax+by=z
# 只要满足z<=x+y并且这样的a和b存在，那么目标就是可以达成的
# ax+by=z有解当且仅当z是x,y的最大公约数的倍数，因此判断x，y的最大公约数是否是z的倍数即可

# 时间复杂度：O(log(min(m,n)))
# 1. math.gcd(x, y)用于计算两个数的最大公约数，其底层实现是基于欧几里得算法。
# 欧几里得算法计算m和n的最大公约数的时间复杂度为O(log(min(m,n)))
# 2. 取模：O(1)

# 空间复杂度：O(1)

class Solution:
    def canMeasureWater(self, x: int, y: int, target: int) -> bool:
        if x+y<target:
            return False
        if target==x or target==y:
            return True
        if x==0 or y==0:
            return False
        return target%math.gcd(x, y)==0
        