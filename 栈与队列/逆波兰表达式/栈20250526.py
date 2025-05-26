# 思路：定义一个栈，每次遇到数字则入栈，遇到计算符号则出栈
# 时间复杂度：O(n)
# 空间复杂度：O(n)

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for token in tokens:
            if token not in {'+', '-', '*', '/'}:
                stack.append(int(token))
            else:
                t1=stack.pop()
                t2=stack.pop()
                if token=='+':
                    stack.append(t1+t2)
                elif token=='-':
                    stack.append(t2-t1)
                elif token=='*':
                    stack.append(t1*t2)
                else:
                    stack.append(t2//t1 if t2*t1>0 else -(abs(t2)//abs(t1)))
        return stack.pop()
        