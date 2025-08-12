# 1. 让num1依次乘上num2的每一位的和
# 2. 将第一步里得到的所有和累加在一起，就可以得到num1*num2的结果
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1=='0' or num2=='0':
            return '0'
        
        total = '0'
        for i, ch in enumerate(num2[::-1]): # 倒序遍历num2
            digit = int(ch)
            product = self.multiply_single(num1, digit)+'0'*i # 123*6+123*50+123*400
            total = self.add_str(total, product)
        return total

    def multiply_single(self, num, digit):
        """将num和单个digit相乘"""
        if digit==0:
            return 0
        result = []
        carry = 0 # 进位值
        for ch in num[::-1]:
            product = int(ch)*digit+carry 
            carry = product//10
            result.append(str(product%10))
        if carry>0:
            result.append(str(carry))
        return "".join(result[::-1])
    
    def add_str(self, a, b):
        """将两个字符串a和b相加"""
        i, j = len(a)-1, len(b)-1
        carry = 0 # 进位值
        result = []
        while i>=0 or j>=0 or carry>0:
            n1 = int(a[i]) if i>=0 else 0
            n2 = int(b[j]) if j>=0 else 0
            tmp = n1+n2+carry
            carry = tmp//10
            result.append(str(tmp%10))
            i-=1
            j-=1
        return "".join(result[::-1])
        