# 思路：从后往前面遍历
# 如果发现str_n[i-1]>str_n[i]，那么就让str_n[i-1]减去1，并且str_n后面的数字都变成9
# 注意：字符串不可改，但是数组可改，所以需要将n变成字符串，然后再变成数组

class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        str_n = list(str(n))
        for i in range(len(str_n)-1, 0, -1):
            if int(str_n[i-1])>int(str_n[i]):
                str_n[i-1] = str(int(str_n[i-1])-1)
                str_n[i:]= '9'*(len(str_n)-i)
        return int(''.join(str_n))