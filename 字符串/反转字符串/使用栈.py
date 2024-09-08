# 方法：使用栈
# 要求空间复杂度为O(1)，因此不能申请其他的数组
# 遍历要求：for(i=0,j=len-1;i<len/2;i++,j--) 
# 然后交换i和j对应的数组
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