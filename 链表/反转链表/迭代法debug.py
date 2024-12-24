# 迭代法（双指针法）
# 思路：当前节点的next指针指向下一个节点，改成当前节点的next指针指向前一个节点，因此需要有一个节点来保存前一个节点
# 初始化，定义nxt为当前节点cur的下一个节点，定义pre为当前节点cur的前一个节点
# 当反转时，令cur.next=pre 然后再pre=cur, cur=nxt

# 定义链表节点
class ListNode(object):
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next

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
    
# 将列表转换为链表
def listtoLink(lst):
    dummy=ListNode() # 虚拟头节点
    current=dummy
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


head=[1,2,3,4,5]
head=listtoLink(head)
print_linkedlist(head)
solution=Solution()
# result=solution.reverseList(head)
