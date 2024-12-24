# 相当于求解区间的并集
# 分析：1. 记录每个元素最后出现的位置（最远的位置） 2. 根据最远的位置确定分界线的位置
# Eg
# 下标：0 1 2 3 4 5 6 7 8 | 9 10 11 12 13 14 15
# 字母：a b a b c b a c a | d  e  f  e  g  d  e
# 最远：8 5 8 5 7 5 8 7 8 | 14 15 11 15 13 14 15
# 第一个区间内end的最大值是8，分割线的位置也是8；第二个区间内end的最大值是15

# 时间复杂度：
# 1. last_occurrence字典初始化：O(n)
# 2. 遍历字符串并计算区间：O(n)
# 总体的时间复杂度为O(n)

# 空间复杂度：
# 1. last_occurrence字典：最坏情况下，字符串s中的字符都是不同的，那么字典将存储n个键值对，O(n)
# 2. result列表：存储每个分割区间的长度，最坏情况同上，O(n)
# 总的空间复杂度为O(n)
class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        last_occurrence={} # 存储每个元素最后出现的位置
        for i,ch in enumerate(s): # list的遍历是通过enumerate实现的
            last_occurrence[ch]=i # i是下标位置
        
        result=[]
        start=0 # 左区间下标
        end=0 # 右区间下标
        for i,ch in enumerate(s):
            end=max(end,last_occurrence[ch]) # 找到当前字符出现的最远位置
            if i==end: # 如果当前位置是最远位置，表示可以分割出一个区间
                # 找到了一个区间，并且该区间内所有字符都只出现在这个区间内
                    result.append(end-start+1) # 计算这个区间的长度，由于区间的下标是由0开始的，因此需要+1
                    start=i+1 # 开始下一个区间
        return result

        