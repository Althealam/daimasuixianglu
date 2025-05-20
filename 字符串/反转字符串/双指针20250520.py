# 思路：定义两个指针，分别指向s的0和len(s)-1的位置，然后对调这两个元素
# 时间复杂度：O(n)
# 空间复杂度：O(1)
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left=0
        right=len(s)-1
        while left<right:
            s[left], s[right]=s[right], s[left]
            # 移动指针
            left+=1
            right-=1
        return s
        