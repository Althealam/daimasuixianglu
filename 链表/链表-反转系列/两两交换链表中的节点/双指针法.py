# 方法：双指针法
# 共性思路：
# 1. 尽可能使用虚拟头节点，可以避免判断节点是否是头节点；
# 2. 删除节点的时候，需要找到被删除节点的前一个节点，然后修改它的next指针，从而跳过要删除的节点
# 双指针的用法：
# 1. slow指针：用于遍历链表，找到需要删除的节点的前一个节点
# 当fast指针到达链表的末尾的时候，slow指针会停在需要删除节点的前一个节点
# 2. fast指针：fast指针先走n+1步，这样slow指针遍历整个链表的同时，fast能够先到达或者超过目标节点
# 一些疑惑：
# 1. 为什么移动fast指针n+1步：可以保证当fast到达链表末尾的时候，slow刚好达到要删除节点的前一个节点
# 2. 为什么fast移动n+1步后，fast和slow同时移动：可以保证它们之间的距离始终为保持n步
# 数学公式推导（假设链表的长度为L，是原始链表的长度，不包括头节点）
# 1. 移动fast n+1步：初始状态，fast和slow都指向虚拟头节点dummy_head
# 2. 同步移动：fast和slow同步移动，假设fast到达链表末尾（链表末尾指的是最后一个节点的next指针所指向的位置）时移动了x步
# 3. 到达末尾：由于fast到达了链表的末尾，所以x=L-(n+1)
# dummy_head 1 2 3 4 5 NULL, L=5, n=2-->(1,2,3,5)
# 4. slow移动的总步数：slow也移动了x步
# 5. 确定slow指向的位置：x=L-(n+1)，slow从虚拟头节点开始，因此这时候slow指向了虚拟头节点开始的L-n个节点，也就是原始链表的L-n+1个节点（也就是倒数第n个节点）


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy_head=ListNode(0,head) # 创建虚拟头节点
        fast=dummy_head # 创建快指针，初始化为虚拟头节点
        slow=dummy_head # 创建慢指针，初始化为虚拟头节点

        # 移动快指针，走n+1步
        for i in range(n+1):
            fast=fast.next
        
        # 移动两个指针，直到快速指针到达链表的末尾
        while fast:
            slow=slow.next
            fast=fast.next

        # 通过更新第(n-1)个节点的next指针删除第n个节点
        slow.next=slow.next.next

        return dummy_head.next

         
        