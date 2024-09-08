# 当我们遇到了要快速判断一个元素是否出现在集合里时，就需要考虑哈希法
# 方法1: 快慢指针法
# 反复调用get_next(n)得到的链表是一个隐式的链表
# 隐式意味着我们没有实际的链表节点和指针，但是数据仍然形成链表结构

# 算法：
# 跟踪链表的两个值，称之为fast指针和slow指针
# 在算法的每一步中，slow在链表中前进1个节点；fast前进2个节点（对get_next函数进行嵌套使用）
# 如果n是一个快乐数，即没有循环，那么fast最终会比slow先到达1
# 如果n不是一个快乐数，那么fast和slow最终会在同一个数上相遇

# fast：每次移动两步，即计算两次数字的下一个状态。
# slow：每次移动一步，即每次计算一次数字的下一个状态（即计算一次数字各位上数字平方和）。

# 时间复杂度：O(logn)
# 空间复杂度：O(1)
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

        slow_runner=n # 第一个节点
        fast_runner=get_next(n) # 第二个节点
        while fast_runner!=1 and slow_runner!=fast_runner:
            # 如果陷入了循环，那么快慢指针会相遇
            # 如果不会陷入循环，那么快指针就会遇到1
            slow_runner=get_next(slow_runner) # slow前进一个节点
            fast_runner=get_next(get_next(fast_runner)) # fast前进两个节点
        return fast_runner==1
# 问题：不会出现slow_runner==fast_runner并且fast_runner=1的情况吗？
# 答案：不会出现。这两个条件是互斥的。
# 1. 快指针先到达1：如果数字序列最终会收敛到1，那么快指针（每次移动两步）会比慢指针（每次移动一步）更早到达1。在这种情况下，循环会结束，并且函数返回True，表明这是一个快乐数
# 2. 快慢指针相遇：如果数字序列不会收敛到1而是进入一个循环，那么快指针和慢指针最终会在某个点相遇。这是因为快指针每次跳过两个状态，而慢指针每次只跳过一个状态，如果它们都进入了同一个循环，快指针最终会追上慢指针。
# 因为相遇意味着它们在循环中，而循环中不会有1。