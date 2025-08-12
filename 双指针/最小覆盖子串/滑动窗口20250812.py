# 思路：滑动窗口+哈希表
# 1. 定义左右指针，指向符合条件的最小覆盖子串的左右端点，也就是ans_left, ans_right
# 2. 定义Counter，用来计算两个子串中每个元素的出现次数
# 3. 如果Counter_s>=Counter_t，则left+=1, counter_s[s[left]]-=1

from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left, right = 0, 0
        start, end = 0, 0 # 记录窗口的起始索引
        counter_s = Counter()
        counter_t = Counter(t)
        min_len = float('inf')
        for right, ch in enumerate(s):
            counter_s[ch]+=1 # 扩展窗口
            while self.is_cover(counter_s, counter_t):
                current_len = right-left+1
                if current_len<min_len: # 更新答案的start和end
                    min_len = current_len
                    start = left
                    end = right
                # 缩小窗口
                counter_s[s[left]]-=1
                left+=1
        return "" if min_len == float('inf') else s[start:end+1]
    
    def is_cover(self, counter_s, counter_t):
        """判断counter_s是否覆盖了counter_t"""
        for ch, count in counter_t.items():
            if counter_s.get(ch, 0)<count:
                return False
        return True
        