# 时间复杂度：O(nlogn)
# 1. 统计元素出现次数：O(n)
# 2. 排序并选取前面k个元素：O(nlogn)
# 空间复杂度：O(n+k)
# 1. 存储元素计数的字典：O(n)
# 2. 存储排序结果：O(k)
from collections import defaultdict
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count=defaultdict(int)
        # 1. 统计每个元素出现的次数
        for item in nums:
            if item not in count.keys():
                count[item]=1
            else:
                count[item]+=1
        # 2. 对字典的value进行排序，并且返回字典中出现频率前k个元素
        sorted_count=sorted(count.items(),key=lambda x:x[1],reverse=True)[:k]
        return [item[0] for item in sorted_count]

## 注意:count.items()和count.values()有区别
# 1. count.items():
# count={'a':1,'b':2} count.items()将会返回dict_items([('a',1),('b',2)])
# 2. count.values():
# 返回字典count的所有值
# count={'a':1,'b':2} count.values将会返回dict_values([1,2])