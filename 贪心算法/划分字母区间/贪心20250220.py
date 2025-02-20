# 思路：
# 1. 遍历s，用hash来统计每个字母的最后一个字符出现的位置
# 2. 遍历字符串，如果找到之前遍历过的所有字母的最远边界，说明这个边界就是分割点

# 时间复杂度：O(n)
# 1. 构建哈希表：O(n)
# 2. 遍历字符串寻找分割点：O(n)
# 空间复杂度：O(n)
# 1. 哈希表distance：O(1) 字符串的字符种类优先，因此哈希表的空间是常数级别的
# 2. 列表result：O(n)

class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        # 存储每个字符最后出现的位置
        distance={}
        for i in range(len(s)):
            distance[s[i]]=i
        
        # 遍历字符串
        result=[] # 列表，存储每个划分出的子字符串的长度
        start=0 # 当前划分的子字符串的起始索引
        end=0 # 当前划分的子字符串的结束索引
        for i, ch in enumerate(s):
            end=max(end, distance[ch]) # 更新end的值，确保end是当前已遍历过的所有字符串最后出现位置的最大值
            # 如果位置到达了end，说明抵达了分割点
            if i==end:
                result.append(end-start+1)
                start=i+1
        return result

        
            
