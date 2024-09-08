# 方法一：双指针法
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# 思路： 用双指针进行递归，让第一个节点指向第二个节点变成第二个节点指向第一个节点
# 时间复杂度：O(n)，其中n是链表中的节点数
# 因为算法需要遍历整个链表一次，对每个节点执行一次指针反转的操作
# 空间复杂度：O(1) 只是用了几个指针变量cur、pre和temp
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # cur：指向头节点
        # pre：初始化为None
        cur=head
        pre=None
        while cur:
            # 反转指针方向
            temp=cur.next # 保存cur的下一个节点
            cur.next=pre # 反转
            # 更新pre和cur节点
            pre=cur
            cur=temp
        return pre
        