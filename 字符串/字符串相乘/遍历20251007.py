# 1. 让num1依次乘上num2的每一位
# 2. 将第一步里得到的所有和累加在一起
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1=='0' or num2=='0':
            return '0'
        total = '0'
        for i, ch in enumerate(num2[::-1]):
            digit = int(ch)
            product = self.multiply_string(num1, digit)+'0'*i
            total = self.add_str(total, product)
        return total
    
    def multiply_string(self, num, digit):
        if digit=='0':
            return '0'
        result = []
        carry = 0 
        for ch in num[::-1]:
            product = int(ch)*digit+carry
            carry = product//10
            result.append(str(product%10))
        if carry>0:
            result.append(str(carry))
        return "".join(result[::-1])
    
    def add_str(self, a, b):
        i, j = len(a)-1, len(b)-1
        carry = 0
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
        