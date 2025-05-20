# 思路：使用栈，遇到元素则弹入，最后弹出元素
# 时间复杂度：O(n)
# 空间复杂度：O(1)
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        stack=[]
        for char in s:
            stack.append(char)
        for i in range(len(stack)):
            s[i]=stack.pop()
        return s