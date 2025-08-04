# 思路：
# 1. 让num1依次乘上num2的每一位的和
# 2. 把第一步里得到的所有和累加在一起，可以得到num1*num2的结果

# 时间复杂度：O(mxn+mxnxk)，其中m为num1的长度，n为num2的长度
# 1. 分层循环，遍历num2的每一位，循环次数为n
# 2. multiply_single函数：O(m)
# 3. 补零操作：最多为n-1，每次补零生成的字符串长度为m+i，但是字符串拼接的时间复杂度为O(m+i)
# 4. add_str函数：每次累加的两个字符串长度分别为：
# （1）前一次total长度：最多m+n
# （2）当前product长度：m+i，最大为m+n-1

# 空间复杂度：O(m+n)
# 1. 存储中间结果的字符串：product和total的最大长度均为m+n
# 2. 函数内部的临时变量：result列表最长为m+n
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1=='0' or num2=='0':
            return '0'

        # 用num2的每一位乘num1，再累加
        total = "0"
        for i, c in enumerate(num2[::-1]):
            digit = int(c)
            product = self.multiply_single(num1, digit)+'0'*i # 注意补零操作
            total = self.add_str(total, product) # 将原来的total和新计算的数值相加在一起
        return total

    def multiply_single(self, num_str, digit):
        """
        字符串数字和单个数字相加
        :num_str: 被乘的字符串数字
        :digit: 乘数，单个数字
        """
        if digit==0:
            return "0"
        result = []
        carry = 0
        for c in num_str[::-1]:
            product = int(c)*digit+carry
            carry = product//10
            result.append(str(product%10))
        if carry>0:
            result.append(str(carry))
        return "".join(result[::-1])
    
    def add_str(self, a, b):
        """两个字符串数字相加"""
        result = []
        i, j = len(a)-1, len(b)-1
        carry = 0 # 进位值
        while i>=0 or j>=0 or carry>0:
            n1 = int(a[i]) if i>=0 else 0
            n2 = int(b[j]) if j>=0 else 0
            total = n1+n2+carry
            carry = total//10
            result.append(str(total%10)) 
            i-=1
            j-=1
        return "".join(result[::-1])



