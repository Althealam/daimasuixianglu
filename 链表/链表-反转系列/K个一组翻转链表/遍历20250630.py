# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 反转逻辑：通过pre和cur逐节点反转，每次将cur指向pre，并更新指针位置
# 连接操作：
# （1）p0始终指向前一组的最后一个节点（初始为dummy_head）
# （2）p0.next.next=cur：将反转后的尾节点连接到当前cur（下一组的头节点）
# （3）p0.next=pre：将前一组的尾节点连接到反转后的新头节点
# 处理剩余节点：当剩余节点数不足K的时候，直接退出循环，保持原来的顺序

# 时间复杂度：O(n)
# 空间复杂度：O(1)
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # 1. 求出链表个数
        n=0
        cur=head
        while cur:
            n+=1
            cur=cur.next
        
        # 2. 反转链表
        dummy_head=ListNode(next=head)
        p0=dummy_head
        while n>=k:
            n-=k
            # 反转k个节点
            pre=None # 待翻转链表的前面一个节点
            cur=p0.next # 待翻转链表的头节点
            for _ in range(k): # 开始反转k个节点
                # 反转
                nxt=cur.next
                cur.next=pre
                pre=cur
                cur=nxt

            # （1）连接右边
            nxt=p0.next # 记录当前段的原头节点    
            p0.next=pre # 现在段的尾节点->反转后的头
            # （2）连接左边
            nxt.next=cur
            # 更新p0位当前段的原头节点
            p0=nxt
        return dummy_head.next