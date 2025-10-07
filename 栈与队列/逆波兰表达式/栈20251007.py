class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in range(len(tokens)):
            if tokens[i] not in ['+', '-', '*', '/']:
                stack.append(int(tokens[i]))
            else:
                n1 = int(stack.pop())
                n2 = int(stack.pop())
                if tokens[i]=='+':
                    tmp = n1+n2
                elif tokens[i]=='-':
                    tmp = n2-n1
                elif tokens[i]=='*':
                    tmp = n1*n2
                else:
                    if n1==0:
                        return None
                    else:
                        tmp = n2//n1 if n2//n1>0 else -(abs(n2)//abs(n1))
                stack.append(tmp)
        return stack.pop()