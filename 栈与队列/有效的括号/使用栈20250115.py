# 思路：
# 定义一个栈，每次遇到括号则将左括号入栈，当遇到对应的括号的时候则出栈
# 不匹配的情况
# 1. 字符串里左括号多余了，不匹配（遍历字符串的时候栈已经为空了）
# 2. 括号没有多余，但是括号的类型不匹配（遍历字符串的时候栈已经为空了，但是字符串还没有遍历完毕）
# 3. 字符串里右括号多余了，不匹配（遍历完字符串后，最后栈内不为空）
# 字符串遍历完后，栈为空则代表左括号和右括号完全匹配了

# 时间复杂度：O(n) 遍历字符串
# 空间复杂度：O(n) 用stack来存储数据
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack=[]
        for item in s:
            if item=='(':
                stack.append(')')
            elif item=='{':
                stack.append('}')
            elif item=='[':
                stack.append(']')
            elif stack is not None and stack[-1]!=item:
                return False
            else:
                stack.pop()
        # not stack表示当stack为空的时候为True，否则当stack不为空的时候为False
        # 如果遍历完字符串了，栈刚好也为空，则代表所有的括号都匹配成功了；如果遍历完字符串后，栈不为空，则表示匹配不成功
        return True if stack is not None else False

        