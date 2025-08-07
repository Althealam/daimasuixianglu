# 思路：
# 1. 定义单调栈，栈中存储没有找到下一个最大元素的元素下标值
# 2. 遍历数组
# （1）如果找到了比i更大的元素下标right，那么弹出栈顶元素，并且找到了right_max；此时如果stack不为空，那么left_max = st[-1]
# （2）如果没有找到比i更大的元素下标，则继续加入i，单调栈内保持单调递减
# 3. 计算当前水柱的体积
# （1）height = min(right_max_height, left_max_height)-bottom_height
# （2）length = i-left_max-1 
# 4. 计算ans：ans+=height*length
class Solution:
    def trap(self, height: List[int]) -> int:
        st = []
        ans = 0 # 雨水的体积
        for i in range(len(height)):
            while len(st)!=0 and height[i]>height[st[-1]]:
                right_max = i
                bottom = st.pop()
                if len(st)!=0:
                    left_max = st[-1]
                    h = min(height[right_max], height[left_max])-height[bottom]
                    l = i-left_max-1
                    ans+=h*l
            st.append(i)
        return ans
        