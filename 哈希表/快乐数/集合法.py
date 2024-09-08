# 当我们遇到了要快速判断一个元素是否出现在集合里时，就需要考虑哈希法
# 方法1:集合法
# 1. 初始化集合set，把n加入set
# 2. 把n替换为它每个位置上的数字的平方和，并加入set
# 3. 重复这个过程一直到新出现的数字等于1时返回true，或者新出现的数字已经存在set中时就返回false
# 会出现三种可能：
# 1. 最终会得到1
# 2. 最终会进入循环
# 3. 值会越来越大，最后接近无穷大
# 算法的两个部分：
# 1. 给一个数字n，它的下一个数字是什么？
# 2. 按照一系列的数字判断是否进入了一个循环
# 时间复杂度：
class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def get_next(n):
            total_sum=0 # 用于存储数字的平方和
            while n>0:
                n, digit=divmod(n,10) # 使用divmod函数将n除以10，并返回商和余数
                total_sum+=digit**2 # 将digit的平方和加到total_sum上
            return total_sum # 返回计算得到的平方和

        seen=set() # 初始化一个集合seen，用于存储已经出现过的数字，以避免无限循环
        while n!=1 and n not in seen:
            # 使用一个循环来重复替换数字，直到数字变为1或者发现数字已经在seen集合中出现过（意味着进入了循环）。
            seen.add(n) # 将当前的数字n添加到seen集合里
            n=get_next(n) # 调用get_next函数计算下一个数字，并更新n的值

        return n==1 # 如果最终n变为1，则返回True，表示这是一个快乐数