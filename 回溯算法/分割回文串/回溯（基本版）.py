# 分析：回文串指的是具有对称性的字符串，我们可以通过绘制树形图对字符串进行切割
# 递归三部曲：
# 1. 递归的参数和返回值：定义两个全局变量，定义一维数组path，存放单一的分割方案；定义二维数组result，来存放所有的分割方案
# 同时还需要startIndex来记录在字符串中下一次切割的位置（startIndex就是切割线）
# 2. 递归终止的条件：切割线切到了字符串最后面，说明找到了一种切割方法
# 3. 单层递归的逻辑：注意需要判断回文子串
# 难点：1. 切割问题可以抽象为组合问题 2. 如何模拟那些切割线 3. 切割问题中递归如何终止 4. 在递归循环中如何截取子串 5. 如何判断回文

# 时间复杂度：
# 1. 回溯过程
# 2. 回文检查：每次检查一个子串是否为回文时，调用了is_palindrome函数，该函数在最坏情况下需要O(n)的时间，其中n是当前子串的长度（即s[start:end+1])
# 3. 回溯的分支数：每次递归都有多个选择，最多是从当前startIndex到字符串末尾的每个位置进行切割，因此总的递归分支数是2^n（即字符串的长度n）
# 总体时间复杂度：
# （1）对于每个分支，最坏情况下会有一个长度为O(n)的回文检查
# （2）总的时间复杂度为O(2^n*n)，其中2^n是可能的切割位置数量，n是每个回文子串的检查时间
# 空间复杂度：
# 1. 递归栈的空间：回溯算法回产生递归栈，递归的深度最大为n
# 2. 存储路径的空间：path，最大长度为n
# 3. 总的空间复杂度：O(n)

class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        递归用于纵向遍历
        for循环用于横向遍历
        当切割线迭代至字符串末尾，说明找到一种方法
        类似组合问题，为了不重复切割同一位置，需要startIndex来做标记下一轮递归的起始位置（切割线）
        """
        result=[]
        self.backstracking(0,result,[],s)
        return result

    def backstracking(self,startIndex,result,path,s):
        if startIndex==len(s):
            result.append(path[:])
            return
        # 单层递归逻辑
        for i in range(startIndex,len(s)):
            # 比其他的组合问题多了一步判断
            if self.is_palindrome(s,startIndex,i):
                path.append(s[startIndex:i+1])
                self.backstracking(i+1,result,path,s)
                path.pop() # 回溯
            
    def is_palindrome(self,s,start,end):
        i=int(start)
        j=int(end)
        while i<j:
            if s[i]!=s[j]:
                return False
            i+=1
            j-=1
        return True
        

        