# 逆波兰表达式就是后缀表达式
# 后缀表达式就是二叉树的后序遍历（左右中）
# Eg：中序表达式：（1+2）x（3+4）
# 二叉树：x
#     +    +
#   1  2  3  4
# 后序遍历：12+34+x，后缀表达式不用加括号，可以直接顺序处理字符串就可以计算出结果

# 本题目中给的逆波兰表达式都是合法的，因此不需要判断是否合法

# 思路：遇到数字就入栈，遇到计算符号就将数组弹出栈并利用该符号进行计算，然后将计算结果入栈
# 遇到数字就入栈，遇到计算符就出栈两个元素并计算

# 分析：栈适合做消除操作，类比左右括号匹配

# 时间复杂度：O(n)，其中n是tokens的长度，每个元素都会被遍历一次
# 空间复杂度：O(n)，其中n是tokens的长度，因为最坏的情况下，栈可能需要存所有的操作数
# 最坏的情况：包含大量的操作数，并且没有立即可以执行的运算，并且运算符的数量比较少

from operator import add, sub, mul

def div(x,y):
    # 使用整数除法的向零取整方式
    # 如果两个数的乘积为正，直接返回整数除法的结果
    # 如果两个数的乘积为负，返回负数除法的结果
    return int(x/y) if x*y>0 else -(abs(x)//abs(y))

class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        # 定义一个字典，用于将字符串形式的预算符映射到相应的操作函数
        op_map={'+':add, '-':sub, '*':mul, '/':div}

        def evalRPN(self, tokens: List[str])->int:
            stack=[]
            for token in tokens:
                # 如果当前元素不是运算符，那么它是一个操作符，将其转换为整数并且压入栈中
                if token not in {'+','-','*','/'}:
                    stack.append(int(token))
                else:
                    # 如果当前元素时运算符，从栈中弹出两个操作数op1和op2
                    # 使用op_map字典中对应的函数进行计算，并将结果压回栈中
                    op2=stack.pop()
                    op1=stack.pop()
                    stack.append(self.op_map[token](op1,op2))
            return stack.pop() # 栈顶的元素就是表达式的结果