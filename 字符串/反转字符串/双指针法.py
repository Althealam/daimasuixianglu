# 方法：双指针法
# 要求空间复杂度为O(1)，因此不能申请其他的数组
# 遍历要求：for(i=0,j=len-1;i<len/2;i++,j--) 
# 然后交换i和j对应的数组
class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        left,right=0,len(s)-1

        # 这个方法不用判断奇偶数，并且空间复杂度比for i in range(len(s)//2)更低
        # while每次每次循环需要进行条件判断，range函数不需要，因此时间复杂度更低
        while left<right:
            s[left],s[right]=s[right],s[left]
            left+=1
            right-=1