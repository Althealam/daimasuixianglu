# 思路：从后往前遍历
# 遍历的时候判断str_n[i]和str_n[i-1]的值：如果str_n[i-1]>str_n[i]，那么就将str_n[i]变成9，然后str_n[i-1]减去1

# 注意：字符串不可改，但是数组可改，所以需要将n变成字符串，然后再变成数组

class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        str_n=list(str(n))
        for i in range(len(str_n)-1, 0, -1):
            if str_n[i-1]>str_n[i]:
                str_n[i-1]=str(int(str_n[i-1])-1)
                str_n[i:]='9'*(len(str_n)-i)
        return int(''.join(str_n))
