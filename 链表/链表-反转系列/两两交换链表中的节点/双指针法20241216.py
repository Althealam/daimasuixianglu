# 思路：迭代法
# 1-2-3-4
# 2-1-3-4
# 2-3-1-4
# 2-3-4-1

# 令temp表示当前到达的节点，初始时temp=dummy_head每次交换temp后面的两个节点
# 如果temp后面没有节点或者只有一个节点，则没有更多的节点要交换，因此结束交换；否则交换temp后面的两个节点
# temp-node1-node2变成temp-node2-node1

# 总体的交换代码：
# temp.next=node2
# node1.next=node2.next
# node2.next=node1

# 时间复杂度：O(n)，需要对每个节点进行更新指针的操作
# 空间复杂度：O(1)

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution(object):
    def swapPairs(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy_head=ListNode(next=head)
        temp=dummy_head # 目前正在遍历的节点

        while temp.next and temp.next.next:
            node1=temp.next
            node2=temp.next.next

            temp.next=node2
            node1.next=node2.next
            node2.next=node1

            temp=node1 # 移动到第二个节点去

        return dummy_head.next

