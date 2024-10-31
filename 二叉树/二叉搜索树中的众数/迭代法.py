# 方法：迭代法
# 注意：本题中二叉树可以出现重复的元素，并且众数并不一定只有一个

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def findMode(self, root):
        st=[]
        cur=root
        pre=None
        maxCount=0 # 最大频率
        count=0 # 统计频率
        result=[]

        while cur is not None or st:
            if cur is not None: # 指针来访问节点，访问到最底层
                st.append(cur) # 将访问的节点放进栈
                cur=cur.left # 左
            else:
                cur=st.pop()
                if pre is None: # 第一个节点
                    count=1
                elif pre.val==cur.val: # 与前一个节点数值相同
                    count+=1
                else: # 与前一个节点的数值不同
                    count=1
                
                if count==maxCount: # 如果和最大值相同，放进result中
                    result.append(cur.val)
                
                if count>maxCount: # 如果计数大于最大值频率
                    maxCount=count # 更新最大频率
                    result=[cur.val]
                
                pre=cur
                cur=cur.right # 右
        return result