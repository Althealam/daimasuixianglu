# 思路：设置i和j分别指向num1和num2的尾部，模拟人工加法
# 1. 计算进位：计算carry=tmp//10，代表当前位相加是否产生进位
# 2. 添加当前进位：tmp = n1+n2+carry，并将tmp%10添加到尾部，然后tmp//10是进位值
# 3. 索引溢出处理：当指针i或者j走到数字首部后，给n1, n2赋值为0，相当于给num1、num2中长度较短的数字前面填0
# 4. 当遍历完num1和num2后跳出循环，并根据carry值决定是否在头部添加进位1，最后返回res即可

# 时间复杂度：O(max(M, N)) 其中M、N分别为num1和num2的长度
# 空间复杂度：O(1)
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        res = ""
        i, j, carry = len(num1)-1, len(num2)-1, 0
        # carry为进位值
        while i>=0 or j>=0:
            n1 = int(num1[i]) if i>=0 else 0
            n2 = int(num2[j]) if j>=0 else 0
            tmp = n1+n2+carry
            carry = tmp//10
            res = str(tmp%10)+res 
            i, j = i-1, j-1
        return "1"+res if carry else res 