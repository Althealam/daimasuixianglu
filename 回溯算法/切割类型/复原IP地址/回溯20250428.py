# 本题二叉树的最大深度为4（因为只有4个子串来组成IP地址）
# 时间复杂度：O(1)
# 1. 回溯过程：IP地址由4个部分组成，总的可能的分割方案熟练是有限的
# 2. 有效性检查：k是子串的长度，子串长度最大为3（因为子串不超过255），因此isvalid的时间复杂度为O(1)

# 空间复杂度：O(1)
# 1. 递归调用栈的深度：取决于IP地址的部分数量，因为每个IP地址固定由4个部分组成，因此递归的最大深度为4
# 2. 存储结果的空间：有效的IP地址的组合数量是固定的，最多是3^4种，并且每个IP地址的长度也是固定的（最多15个字符），因此存储结果的空间复杂度为O(1)

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        result=[]
        path=[]
        self.traversal(result,path, s, 0)
        return result
    
    def traversal(self, result, path, s, startIndex):
        if startIndex==len(s) and len(path)==4:
            result.append('.'.join(path[:]))
            return 
        for i in range(startIndex, len(s)):
            x=s[startIndex:i+1]
            if self.isvalid(x):
                path.append(x)
                self.traversal(result, path, s, i+1)
                path.pop()
    
    def isvalid(self, x):
        # 1. 整数在0到255之间
        if int(x)>255 or int(x)<0:
            return False
        # 2. 整数不是0，并且包含前导0
        if x!='0' and x[0]=='0':
            return False
        return True