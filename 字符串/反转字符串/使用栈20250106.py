# 思路：使用栈来解决
# 把所有的元素进栈，然后依次出栈就可以得到反转后的字符串
# 时间复杂度：O(n)
# 空间复杂度：O(n)，栈需要空间，需要将输入列表s中的所有元素依次压入

class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        stack=[]
        for char in s:
            stack.append(char)
        for i in range(len(s)):
            s[i]=stack.pop()
        return s
