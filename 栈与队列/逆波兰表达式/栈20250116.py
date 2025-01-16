# 思路：遇到数字则入栈，遇到符号则弹出栈顶的两个元素，并用符号进行计算（第一个出栈的元素放到分母的位置，或者是第二个位置），计算完后将计算结果入栈
# 时间复杂度：O(n)
# 空间复杂度：O(n)，用栈来存储元素

class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack=[]
        for item in tokens:
            if item not in {'+','-','*','/'}:
                stack.append(int(item))
            elif item=='+':
                op1=stack.pop()
                op2=stack.pop()
                stack.append(op1+op2)
            elif item=='-':
                op1=stack.pop()
                op2=stack.pop()
                stack.append(op2-op1)
            elif item=='*':
                op1=stack.pop()
                op2=stack.pop()
                stack.append(op1*op2)
            elif item=='/':
                op1=stack.pop()
                op2=stack.pop()
                if op1*op2>0:
                    result=op2//op1
                else:
                    result=-(abs(op2)//abs(op1))
                stack.append(result)
        return stack.pop()             

     

tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]

solution=Solution()
result=solution.evalRPN(tokens)