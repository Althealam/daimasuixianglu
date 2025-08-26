class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_appearance = {} # 每个字符的最远出现下标
        for i in range(len(s)):
            last_appearance[s[i]] = i
        res = []
        start = 0 # 分割片段的起始位置
        end = 0 # 分割片段的结束位置
        for i in range(len(s)):
            end = max(end, last_appearance[s[i]])
            if i==end: # 到达了分割位置
                res.append(end-start+1)
                start = i+1
        return res
        