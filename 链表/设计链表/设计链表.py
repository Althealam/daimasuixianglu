# 代码还有点问题
class ListNode:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next

class MyLinkedList(object):

    def __init__(self):
        # 初始化空链表
        self.dummy_head=ListNode()
        self.size=0

    def get(self, index):
        # 获取链表第index个节点的数值
        """
        :type index: int
        :rtype: int
        """
        if index<0 or index>self.size:
            return -1
        
        current=self.dummy_head.next
        for i in range(index):
            current=current.next
        # 确保current不是None

        return current.val if current else -1

    # 在链表的最前面插入一个节点，节点的值为val
    def addAtHead(self, val):
        """
        :type val: int
        :rtype: None
        """
        new_node=ListNode(val,self.dummy_head.next)
        self.dummy_head.next=new_node
        self.size+=1

    
    # 在链表的最后面插入一个节点
    def addAtTail(self, val):
        """
        :type val: int
        :rtype: None
        """
        current=self.dummy_head
        while current.next:
            current=current.next
        current.next=ListNode(val)
        self.size+=1


    
    # 在链表的第index个节点前面插入一个节点
    def addAtIndex(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        if index<0 or index>self.size:
            return 
        if index==0:
            self.addAtHead(val)
        else:
            current=self.dummy_head
            for i in range(index):
                current=current.next
            current.next=ListNode(val,current.next)
        self.size+=1

    # 删除链表的第index个节点
    def deleteAtIndex(self, index):
        """
        :type index: int
        :rtype: None
        """
        if index<0 or index>=self.size:
            return

        current=self.dummy_head
        if index==0:
            self.dummy_head.next=self.dummy_head.next.next
        else:
            # 找到要插入的位置
            for i in range(index-1):
                current=current.next
            # 删除当前节点的下一个节点
            current.next=current.next.next
        self.size-=1




# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)