{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# 方法：递归法-前序遍历-新建root\n",
    "# 1. 确定递归函数的参数和返回值：传入两个二叉树的根节点，返回值就是合并之后二叉树的根节点\n",
    "# 2. 确定终止条件：t1==NULL时为t2；t2==NULL时为t1\n",
    "# 3. 确定单层递归的逻辑：将两棵树的元素加到一起\n",
    "# 合并规则：如果有相同的节点，就将两个节点合并相加\n",
    "# 思路：利用前序遍历来处理两棵树（中序和后序也可以，只是前序比较直观）\n",
    "\n",
    "# 时间复杂度：O(n)\n",
    "# 代码使用递归方法遍历两棵二叉树，对于每个节点，都会进行一次递归调用\n",
    "\n",
    "# 空间复杂度：O(n)\n",
    "# 空间复杂度包含两部分：递归调用栈的深度和创建新节点所占的空间。\n",
    "# 1. 递归调用栈：每次递归调用会在栈中存储一层，深度最多等于树的高度 h。\n",
    "# （1）平衡树为O(logn)\n",
    "# （2）不平衡树（链状）为O(n)\n",
    "# 2. 新节点的创建：由于代码为合并结果创建了一个新的树结构，合并后的树中包含 n 个节点，每个节点占用常量空间。\n",
    "\n",
    "# Definition for a binary tree node.\n",
    "# class TreeNode(object):\n",
    "#     def __init__(self, val=0, left=None, right=None):\n",
    "#         self.val = val\n",
    "#         self.left = left\n",
    "#         self.right = right\n",
    "class Solution(object):\n",
    "    def mergeTrees(self, root1, root2):\n",
    "        \"\"\"\n",
    "        :type root1: Optional[TreeNode]\n",
    "        :type root2: Optional[TreeNode]\n",
    "        :rtype: Optional[TreeNode]\n",
    "        \"\"\"\n",
    "        if not root1:\n",
    "            return root2\n",
    "        if not root2:\n",
    "            return root1\n",
    "        root=TreeNode() # 创建新节点\n",
    "        root.val=root1.val+root2.val\n",
    "        root.left=self.mergeTrees(root1.left,root2.left)\n",
    "        root.right=self.mergeTrees(root1.right,root2.right)\n",
    "\n",
    "        return root # 返回新节点\n",
    "        "
   ]
  }
 ],
 "metadata": {
  "language_info": {
   "name": "python"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
