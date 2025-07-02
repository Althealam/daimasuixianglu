# 思路：设置双指针分别指向num1和num2的尾部，模拟人工加法
# 时间复杂度：O(max(m, n)) 其中m和n分别为数字的长度
# 空间复杂度：O(1)

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        res = ""
        i, j, carry = len(num1)-1, len(num2)-1, 0 # carry为进位值
        while i>=0 or j>=0:
            n1 = int(num1[i]) if i>=0 else 0
            n2 = int(num2[j]) if j>=0 else 0
            tmp = n1+n2+carry # 当前位置的值
            carry = tmp//10 # 进位值
            res = str(tmp%10)+res
            i, j = i-1, j-1
        return "1"+res if carry else res
        