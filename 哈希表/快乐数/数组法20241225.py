# 分析：由证明可以知道，只会出现两种情况（不会出现越来越大而趋于正无穷的情况）
# 1. 最终和趋于1
# 2. 最终进入一个死循环里
# 思路：
# 1. 给定数字n，下一个数字是什么
# 2. 按照一系列的数字判断是否进入了一个死循环
class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # 1. 给定数字n的情况下，计算下一个数字
        def get_next_n(n):
            new_num=0
            if n>0:
                str_n=str(n)
                for i in str_n:
                    new_num+=int(i)**2
            return new_num
        
        # 2. 判断是否进入了死循环（利用哈希表，存储出现过的数字，只要有一个数字出现过（除了1），就说明进入了死循环，进入死循环时直接返回False）
        seen_num=[] # 用来存储出现过的数字
        while n!=1 and n not in seen_num: 
            seen_num.append(n)
            n=get_next_n(n)
        return n==1