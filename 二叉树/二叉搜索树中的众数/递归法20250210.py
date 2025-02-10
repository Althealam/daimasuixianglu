# 思路：
# 1. 用中序遍历获取二叉搜索树的有序数组
# 2. 统计数组中每个元素的出现频率（用字典来实现）
# 3. 找到出现频率最大的元素的出现频率
# 4. 返回出现频率最大的元素

# 时间复杂度：O(n)
# 1. 中序遍历阶段：O(n)
# 2. 统计元素频率：O(n)
# 3. 寻找最大频率元素：O(n)

# 空间复杂度：O(n)
# 1. 递归调用栈：O(h)
# 2. 存储中序遍历结果的列表空间self.vector：O(n)
# 3. 存储元素频率的字典空间cnt：O(n)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def __init__(self):
        self.vector=[]
    
    def traversal(self,root):
        if root is None:
            return
        self.traversal(root.left)
        self.vector.append(root.val)
        self.traversal(root.right)

    def findMode(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        # 获取中序数组
        self.vector=[]
        self.traversal(root)

        # 统计每个元素出现的频率
        cnt=defaultdict(int)
        result=[]
        for item in self.vector:
            if item not in cnt:
                cnt[item]=1
            else:
                cnt[item]+=1
        
        # 找出现频率最多的元素
        max_freq=max(cnt.values())
        for key, freq in cnt.items():
            if freq==max_freq:
                result.append(key)
        return result
        

        