# 思路：
# 1. 定义一个单调栈，栈内的元素是还没找到答案的元素的下标
# 2. 遍历一个元素和栈顶元素比较，如果该元素值大于等于栈顶元素，则弹出栈顶元素，并弹入该元素，更新栈顶元素的答案值
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans=[0]*len(temperatures)
        stack=[]
        for i in range(len(temperatures)):
            while stack and temperatures[stack[-1]]<temperatures[i]:
                ans[stack[-1]]=i-stack[-1]
                stack.pop()
            stack.append(i)
        return ans