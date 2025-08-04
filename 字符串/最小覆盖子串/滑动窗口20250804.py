# 覆盖的定义：s的子串BACN中每个字母的出现次数都大于等于t=ABC中每个字母的出现次数
# 1. 定义left=-1, right=m，表示最短子串的左右端点
# 2. 用一个哈希表统计t中每个字母的出现次数
# 3. 初始化left=0, 以及一个哈希表cntS，用来统计s子串中每个字母的出现次数
# 4. 遍历s，假设当前子串右端点为right，将s[right]的出现次数cnt_s[s[right]]加1
# 5. 遍历cntS中每个字母以及出现次数，如果出现次数都大于等于cntT中的字母出现次数，则更新ans的值，cnt_s[s[left]]-=1, left+=1


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # 最短覆盖子串的左右端点
        ans_left = -1
        ans_right = len(s)
        cnt_s = Counter()
        cnt_t = Counter(t) # 统计t中每个字母的出现次数

        left = 0 # 开始寻找最短子串
        for right, ch in enumerate(s):
            cnt_s[ch]+=1
            while cnt_s>=cnt_t: # 找到了覆盖子串，开始缩短滑动窗口
                if right-left<ans_right-ans_left: # 当前是最短覆盖子串
                    ans_right, ans_left = right, left
                # 移动左子串
                cnt_s[s[left]]-=1
                left+=1
        return '' if ans_left<0 else s[ans_left:ans_right+1]

        