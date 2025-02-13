# 思路：
# 1. 递归函数的参数和返回值：结果集result，路径path，搜索的位置startIndex，字符串s
# 2. 终止条件：if startIndex==len(s): result.append(".".join(path)) return
# 3. 单层搜索的逻辑：检查某一段字符串是否满足条件：x[startIndex:i+1]
# 定义一个isvalid：判断该整数是否在0到255之间（0<x[startIndex:i+1]<255)，判断是否第一个数字为0（不包含0）
# 注意需要剪枝，剪去的枝就是：（1）整数个数超过4 （2）整数个数小于4

# 注意：本题中二叉树的最大深度为4（因为只有4个子串来组成IP地址）
# 时间复杂度：O(1)
# 1. 回溯过程：IP地址由4个部分组成，总的可能的分割方案数量是有限的 O(1)
# 2. 有效性检查：k是子串的长度，子串长度最大为3，因此isvalid的时间复杂度为O(1)


# 空间复杂度：
# 1. 递归调用栈的深度：取决于IP地址的部分数量，因为每个IP地址固定由4个部分组成，因此递归的最大深度为4
# 2. 存储结果的空间：有效的IP地址的组合数量是固定的，最多是3^4种，并且每个IP地址的长度也是固定的（最多15个字符），存储结果的空间复杂度为O(1)

class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        result=[]
        self.backtracking(result, [], 0, s)
        return result
    
    def backtracking(self, result, path, startIndex, s):
        if len(path)>4: # 剪枝：整数个数超过4
            return
        if startIndex==len(s) and len(path)==4: # 剪枝：整数个数不为4
            result.append('.'.join(path[:]))
            return
        for i in range(startIndex, len(s)):
            x=s[startIndex:i+1]
            if self.isvalid(x): # 剪枝，判断是否符合IP地址的定义
                path.append(x)
                self.backtracking(result, path, i+1, s)
                path.pop()
    
    def isvalid(self,x):
        digit_x=int(x)
        if x[0]=='0' and x!='0':
            return False
        if digit_x>255 or digit_x<0:
            return False
        return True
