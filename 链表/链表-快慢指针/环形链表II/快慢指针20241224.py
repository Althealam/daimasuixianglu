# 方法：快慢指针法
# fast指针每次移动两个节点，slow指针每次移动一个节点，如果fast和slow相遇了，则说明有环

# 1. 判断是否有环：fast每次走两步，slow每次走一步，如果fast和slow相遇，则有环
# 2. 判断入环的位置：让index1从相遇的地方出发，index2从head出发，当index1和index2相遇的时候，就是入环的位置
# 注意：if是不会去遍历循环的，只是会去判断条件，因此这道题需要使用while

# 时间复杂度：O(n)，n是链表的长度
# 空间复杂度：O(1)

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # Step1: 判断是否有环（找fast和slow相遇的地方）
        fast=head
        slow=head
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next

            # 有环：达到了相遇的节点
            if fast==slow:
                index1=fast # 从相遇的节点出发的指针
                index2=head # 从开始的节点出发的指针
                # Step2：找入环的位置（只要有环，通过这个while循环一定可以找到入环的位置）
                while index1!=index2:
                    index1=index1.next
                    index2=index2.next
                return index1
        # 没环：遍历完立案表了也没有达到相遇的节点
        return None
