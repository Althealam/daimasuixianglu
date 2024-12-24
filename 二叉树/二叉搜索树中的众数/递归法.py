# 方法：递归法（利用字典）
# 注意：本题中二叉树可以出现重复的元素，并且众数并不一定只有一个

# 时间复杂度：
# 1. 遍历树：searchBST 方法使用前序遍历来遍历树的所有节点，此时的时间复杂度为O(n)
# 2. 统计频率：在遍历过程中，使用freq_map[cur.val]+=1来统计每个节点的频率，这是O(1)
# 3. 找到最大频率：max(freq_map.values())，时间复杂度为O(k)，其中k为不同元素的数量
# 4. 构建结果：最后一个循环遍历freq_map，找到所有频率等于最大频率的元素，这时候是O(k)
# 总的时间复杂度：O(n)+O(k)+O(k)=O(n+k)
# 空间复杂度：
# 1. 频率映射：使用defaultdict(int)来存储元素频率，最坏情况下，所有元素都是不同的，因此freq_map的大小为O(k)
# 2. 递归栈空间：最坏情况下，树为线性的，递归调用的最大深度为n，因此栈空间为O(n)
# 总的空间复杂度：O(k)+O(n)=O(n+k)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import defaultdict

class Solution(object):
    # 前序遍历搜索二叉树
    # cur：遍历的节点
    # freq_map：存储频率值的字典
    def searchBST(self,cur,freq_map):
        if cur is None:
            return
        # 前序遍历
        freq_map[cur.val]+=1 # 统计元素频率
        self.searchBST(cur.left,freq_map) # 左
        self.searchBST(cur.right,freq_map) # 右
    
    def findMode(self, root):
        freq_map=defaultdict(int) # key: 元素 value: 出现的频率
        result=[] # 结果集，用来存储二叉搜索树的众数（不一定只有一个，因此需要数组来存储）
        if root is None:
            return result
        self.searchBST(root,freq_map) # 统计各个节点的出现频率
        max_freq=max(freq_map.values()) # 找到最大的频率值
        for key, freq in freq_map.items():
            if freq==max_freq:
                result.append(key)
        return result

        