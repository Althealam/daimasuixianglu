# 思路：遇到左括号则入栈其对应的右括号，遇到右括号则弹出栈顶元素
# 三种不匹配的情况
# 1. 字符串里左括号多余，因此不匹配
# 2. 字符串里右括号多余，因此不匹配
# 3. 字符串里括号没有多余，但是括号的类型没有匹配上，因此不匹配

# 判断方法：
# 1. 已经遍历完所有字符串，但是栈不为空，因此有左括号没找到匹配的右括号
# 2. 遍历字符串的过程中，发现栈里没有要匹配的字符
# 3. 遍历字符串匹配的过程中，栈已经为空了，没有匹配的字符了，说明有右括号没有找到匹配的左括号
class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for item in s:
            if item=='(':
                stack.append(')')
            elif item=='[':
                stack.append(']')
            elif item=='{':
                stack.append('}')
            elif not stack or stack[-1]!=item: # 没能通过有效的顺序闭合
                return False
            else:
                stack.pop() # 遇到了符合的元素
        return True if not stack else False