# 方法一：虚拟头节点法
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# 思路：需要有一个cur在需要交换的两个节点的前面
# 只能交换指针，不能改变节点的值
# 时间复杂度：O(n/2) 每对节点被交换一次，因此总的交换次数是n/2（对于奇数个节点，最后一个节点不参与交换）
# 空间复杂度：O(1) 虽然使用了虚拟头节点，但是它不依赖于输入链表的大小，因此额外空间是常数级别的
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy_head=ListNode(next=head)
        cur=dummy_head # cur很重要，cur在两个需要反转的节点的前面
        # 可以看视频理解一下这个遍历条件
        # 这个条件对于节点个数是奇数的时候很重要
        # 进行反转节点的操作
        while cur.next and cur.next.next:
            # 保存需要操作的节点的指针
            temp=cur.next # 需要保存节点1的指针
            temp1=cur.next.next.next # 需要保存节点3的指针

            cur.next=cur.next.next # 保存节点2的指针
            cur.next.next=temp
            temp.next=temp1

            # 移动节点进行遍历
            cur=cur.next.next

        return dummy_head.next # 添加了虚拟头节点后，头节点变成是dummy_head


        