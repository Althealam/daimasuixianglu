# 思路：定义栈存储元素，如果当前遍历的元素和栈顶元素相同，则弹出栈顶元素，直到当前遍历的元素和栈顶元素不同
class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            if len(stack)!=0 and s[i]==stack[-1]:
                stack.pop()
            else:
                stack.append(s[i])
        return ''.join(stack[:])

        