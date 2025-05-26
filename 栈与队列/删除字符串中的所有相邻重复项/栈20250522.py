# 思路：每次都入栈元素，如果遇到的元素和栈顶元素相同，则弹出栈顶元素，否则弹入该元素
# 时间复杂度：O(n)
# 空间复杂度：O(1)
class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack=[]
        for char in s:
            if stack and char==stack[-1]:
                stack.pop()
            else:
                stack.append(char)
        return ''.join(stack)
        