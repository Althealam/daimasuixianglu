# 思路：
# 定义一个栈stack，用来存储s中的所有元素
# 遇到元素，首先判断stack的最后一个元素是否和item相同，如果是的话则出栈
# 否则的话，则入栈
# 最后输出stack

# 时间复杂度：O(n)
# 空间复杂度：O(n)
class Solution(object):
    def removeDuplicates(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack=[]
        for item in s:
            if stack and item==stack[-1]:
                stack.pop()
            else:
                stack.append(item)
        return ''.join(stack)
        