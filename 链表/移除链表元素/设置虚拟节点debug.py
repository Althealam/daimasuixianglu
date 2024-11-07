# 设置虚拟节点(debug)
# 思路：current_head来遍历链表，如果遇到了等于val的值，就current_head.next=current_head.next.next

# 定义链表的节点结构
class ListNode(object):
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next

class Solution(object):
    def removeElements(self,head,val):
        dummy_head=ListNode(next=head)
        current_head=dummy_head
        # 开始遍历链表
        while current_head.next:
        # 注意这里判断的是current_head.next.val而不是current_head.val，因为需要有一个节点来记住前面的一个节点
            if current_head.next.val==val:
                current_head.next=current_head.next.next
            else:
                current_head=current_head.next
        return dummy_head.next

# 将列表转换为链表
def list_to_linkedlist(lst):
    dummy=ListNode() # 定义虚拟头节点
    current=dummy # 开始遍历
    for val in lst:
        current.next=ListNode(val)
        current=current.next
    return dummy.next

# 打印链表
def print_linkedlist(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")



solution=Solution()
head=[1,2,6,3,4,5,6]
val=6
head=list_to_linkedlist(head)
print_linkedlist(head)
result=solution.removeElements(head,val)
        