# 思路：
# 1. 统计每个字符最后的出现次数
# 2. 从头遍历字符，更新字符的最远出现下标，如果找到字符最远出现位置下标和当前下标相等，则找到了分割点
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_appearance={} # 用来统计每个字符的最远出现下标
        # 更新每个字符的最远出现下标
        for i in range(len(s)):
            last_appearance[s[i]]=i
        # 更新字符的最远出现下标
        res=[] # 分割片段的长度的集合
        start=0
        end=0
        for i in range(len(s)):
            end=max(end, last_appearance[s[i]]) # 更新每个字符的最远出现下标
            if i==end: # 达到了一个分割点
                res.append(end-start+1) # 将当前片段的长度加入到res中
                start=end+1 # 片段开始位置
        return res


        return last_appearance
        