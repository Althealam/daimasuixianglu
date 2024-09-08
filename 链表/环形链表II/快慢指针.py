# 思路：使用快慢指针（如果没有环，那么快慢指针在走相同的方向的情况下不可能相遇；如果有环，则会在环里相遇）

# 问题1：为什么如果有环的话，快慢指针一定会相遇？
# 答案1：假设快指针每次走2步，慢指针每次走1步，那么快指针相对于慢指针每次走1步（相当于快指针在1个1个节点的逼近慢指针），这就是一个快追慢问题，最后一定会相遇。
# 问题2：为什么慢指针一定会在进入环的第一圈内被追上？
# 答案2：可以将环展开来看，绘制图片可以发现，当慢指针还没走完一圈的时候就会被快指针追上了，因为快指针的速度是慢指针的两倍
# 如果快指针每次走3步，慢指针每次走1步，有可能快指针会没办法在环内与慢指针相遇，因为可能会直接跳过慢指针。

# 推导：假设链表头节点到环入口的距离是x；环入口到两节点相遇的距离是y；两节点相遇到环入口是z；
# slow=x+y fast=x+y+n(y+z) 快慢指针相遇时，快指针已经在环内转了n次了
# 写出等式：2(x+y)=x+y+n(y+z)-->x+y=n(y+z)-->x=n(y+z)-y（快指针至少要在环内走一圈，才能和慢指针相遇，因此n>=1）
# x=(n-1)(y+z)+z
# 这个公式的含义：n=1时，相当于fast指针在环内转了一圈后就遇到了slow指针，也就是x=z
# ！！！这意味着：从头节点出发一个指针，从相遇节点也出发一个指针，当两个指针每次只走一个节点，那么这两个指针相遇的时候就是环形入口的节点。（参考代码随想录的图片，很直观！！！）


# 重点就是：利用快慢指针找到相遇的节点，其中快指针每次走两步，慢指针每次走一步
# 最后找到相遇的节点后，利用相遇的节点来找环形的入口

# 时间复杂度：O(n)，快指针需要在环中转一圈才能和慢指针相遇
# 空间复杂度：O(1)，除了输入的链表外，只需要常数级别的额外空间来存储指针

# Definition for singly-linked list.
# # class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        fast=head
        slow=fast
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
            if fast==slow:
                index1=fast # 相遇的点
                index2=head # 头部的点
                while index1!=index2:
                    index1=index1.next
                    index2=index2.next
                return index1
        return None

        