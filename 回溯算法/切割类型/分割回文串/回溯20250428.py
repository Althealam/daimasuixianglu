# 时间复杂度：O(n*2**(n-1))
# 1. 回溯的调用次数：长度为n的字符串，最坏情况下啊每个位置都可以作为分割点，则有2**(n-1)种不同的分割方案
# 2. 每次回溯调用中的操作
# （1）提取子串：x=s[startIndex:i+1] 最坏情况下子串长度达到n，此时为O(n)
# （2）判断回文：通过x==x[::-1]判断回文，反转字符串的操作的时间复杂度为O(n)
# （3）复制路径：path[:]的操作的时间复杂度为O(n)
# 空间复杂度 O(n*2**n)
# 1. 递归调用栈的空间：递归的深度最大为n，因为每次递归调用都会处理字符串的一个子串，直到处理完整个子串
# 2. 存储结果的空间：最坏情况下有2**(n-1)种分割方案，每种分割方案的子串数量最多为n，每个子串的最大长度为n，因此为O(n*2**n)
# 3. 临时变量的空间：x的空间为O(n)

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result=[]
        path=[]
        self.traversal(result, path, s, 0)
        return result
    
    def traversal(self, result, path, s, startIndex):
        if startIndex==len(s):
            result.append(path[:])
            return 
        for i in range(startIndex, len(s)):
            x=s[startIndex:i+1]
            if self.ishuiwen(x):
                path.append(x)
                self.traversal(result, path, s, i+1)
                path.pop()
        
    def ishuiwen(self, x):
        if x==x[::-1]:
            return True
        return False