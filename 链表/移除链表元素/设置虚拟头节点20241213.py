# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 时间复杂度：O(n)
# 空间复杂度：O(1)

# 定义链表节点
class ListNode(object):
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: Optional[ListNode]
        :type val: int
        :rtype: Optional[ListNode]
        """
        dummy_head=ListNode(next=head) # 虚拟头接待你

        current=dummy_head # 从虚拟头节点开始遍历
        while current.next: # 遍历链表
            if current.next.val==val:
                current.next=current.next.next
            else:
                current=current.next
        return dummy_head.next
    
# 将列表转换为链表
def list_to_linkedlist(lst):
    dummy=ListNode() # 定义一个虚拟头节点
    current=dummy
    for val in lst: # 遍历列表中的元素
        current.next=ListNode(val) # 构建节点
        current=current.next # 移动节点
    return dummy.next # 返回链表

# 打印链表
def print_linkedlist(head_linkedlist):
    current=head_linkedlist
    while current:
        print(str(current.val)+'->')
        current=current.next
    print('None')

solution=Solution()
head=[1,2,3,4,5,6]
val=6
head_linkedlist=list_to_linkedlist(head)
print_linkedlist(head_linkedlist)
result=solution.removeElements(head_linkedlist,val)
print_linkedlist(result)