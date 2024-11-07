# 迭代法
# 思路：当前节点的next指针指向下一个节点，改成当前节点的next指针指向前一个节点，因此需要有一个节点来保存前一个节点

class Solution(object):
    def reverseList(self,head):
        cur=head
        pre=None
        while cur:
            # 反转
            nxt=cur.next # 记录cur的后一个节点
            cur.next=pre 
            # 遍历下一个节点
            pre=cur
            cur=nxt
        return pre
