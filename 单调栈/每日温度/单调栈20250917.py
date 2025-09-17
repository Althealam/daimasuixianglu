# 1. 定义单调栈，栈中存储还没找到下一个更高温度的元素下标
# 2. 遍历所有元素，如果当前元素值比栈顶元素，则弹出栈顶元素，记录栈顶元素的答案值，并且将当前遍历的元素加入单调栈中

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        st = []
        ans = [0]*len(temperatures)
        for i in range(len(temperatures)):
            while len(st)!=0 and temperatures[st[-1]]<temperatures[i]:
                ans[st[-1]] = i-st[-1]
                st.pop()
            st.append(i)
        return ans
        