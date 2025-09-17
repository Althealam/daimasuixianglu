# 1. 定义单调栈，栈中存储还没找到下一个更大元素的元素下标
# 2. 遍历数组元素，判断数组元素和栈顶元素的大小
# （1）当前栈顶元素找到了更大的元素值：弹出栈顶元素，right为当前遍历的元素，left为栈顶元素
# （2）没有找到更大的元素值：继续加入元素到栈中
class Solution:
    def trap(self, height: List[int]) -> int:
        st = []
        ans = 0
        for i in range(len(height)):
            while len(st)!=0 and height[i]>height[st[-1]]:
                right_max = i
                bottom = st.pop()
                if len(st)!=0:
                    left_max = st[-1]
                    h = min(height[right_max], height[left_max])-height[bottom]
                    l = right_max-left_max-1
                    ans+=h*l
            st.append(i)
        return ans
        