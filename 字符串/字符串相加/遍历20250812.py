# 思路：从尾到头遍历num2和num1，定义carry值
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        # 让num2为最短的
        if len(num2)>len(num1):
            num1, num2 = num2, num1
        
        num2_cur = len(num2)-1
        num1_cur = len(num1)-1
        carry = 0 # 进位值
        res = "" # 答案值
        while num1_cur>=0 or num2_cur>=0:
            n1 = int(num1[num1_cur]) if num1_cur>=0 else 0
            n2 = int(num2[num2_cur]) if num2_cur>=0 else 0
            tmp = n1+n2+carry
            carry = tmp//10 # 进位值
            res = str(tmp%10)+res
            num1_cur-=1
            num2_cur-=1
        return res
        

        