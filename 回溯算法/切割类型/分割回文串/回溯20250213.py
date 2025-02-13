# 思路：回文串指的是字符串从左到右读和从右到左读是一样的
# 1. 递归函数的参数和返回值：result结果集，path路径，startIndex下一层搜索的开始位置，s字符串
# 2. 终止条件：当切割线到达数组的最后一个位置的时候则添加path到result中，并返回（startIndex==len(s))
# 3. 单层搜索的逻辑：判断该子串是否是回文的，如果是的话，则添加到path中，并进行递归和回溯
# 判断回文的逻辑：判断子串本身和子串反过来是否是一致的，如果是的话再去进行上述单层搜索的逻辑

# 时间复杂度：O(n*2^n)
# 1. 回文子串判断：使用x==x[::-1]来判断，对于长度为m的子串来说，反转操作和比较操作的时间复杂度为O(m)
# 2. 回溯过程：对于长度为n的字符串，所有可能的分割数量上线是2^(n-1)（在字符串的n-1个间隔中，每个间隔都有两种选择）
# 空间复杂度：O(n*2^n)
# 1. 递归调用栈的深度：取决于字符串的长度n，递归的最大深度为n
# 2. 存储结果的空间：存储所有可能的分割方案，最多右2^(n-1)种分割方案，并且每种方案的所有子串长度为n

class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        result=[]
        self.backtracking(result,[],0, s)
        return result
    
    def backtracking(self, result, path, startIndex, s):
        if startIndex==len(s): # 当startIndex到达字符串最后面的时候，则收割该子串
            result.append(path[:]) # 这里需要添加path的副本path[:]
            return 
        
        for i in range(startIndex, len(s)): # startIndex相当于递归树中的切割线
            x=s[startIndex:i+1] # 注意后面是i+1，表示从startIndex到i的子串
            if self.ishuiwen(x):
                path.append(x)
                self.backtracking(result, path, i+1, s)
                path.pop()

    def ishuiwen(self, x):
        if x==x[::-1]:
            return True
        else:
            return False

        
solution=Solution()
s="aab"
result=solution.partition(s)
print(result)