# 思路：
# 1. 从后往前遍历
# 2. 如果n[i]<n[i-1]：n[i-1]-=1, n[i]=9，并且让i后面的元素都是9，这样才可以保证数字是最大的
# 不可以通过str_n[i]=str(int(str_n[i])-1)的方式来修改字符串，因为字符串是不可修改的对象
# 需要通过new_char=str(int(str_n[i])-1) str_n=str_n[:i-1]+new_char+'9'*(length-i)来构造

# 注意：299也是递增数字
# 332-329(flag=2)-229(flag=1)-299

# 假设整数n的位数为k
# 时间复杂度：O(k^2)
# 1. 字符串转换：O(k)
# 2. 遍历字符串：O(k)
# 3. 拼接字符串：O(k)
# 空间复杂度：O(k)
# 1. 字符串存储：O(k)
# 2. 临时字符串：O(k)

class Solution(object):
    def monotoneIncreasingDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        str_n=str(n)
        flag=0
        length=len(str_n)
        for i in range(len(str_n)-1, -1, -1):
            if i>0 and str_n[i]<str_n[i-1]: # 前一个字符大于后一个字符
                flag=i
                # 字符串是不可变类型，因此不可以直接通过赋值来修改哦
                new_char=str(int(str_n[i-1])-1)
                str_n=str_n[:i-1]+new_char+'9'*(length-i)

        return int(str_n)
        