# 题目要求时间复杂度优于O(nlogn)
# 可以考虑另外一种字典的方法，让复杂度是O(mlogm)，并且m小于n


# 时间复杂度：O(mlogm)
# 1. 统计元素出现次数:O(n)
# 2. 调转键值对存储元素：O(n)
# 3. 排序操作：O(mlogm)
# 4. 构建结果列表并扁平化：O(m)

# 空间复杂度：O(n+k)
# 1. 存储元素出现次数的字典：O(n)
# 2. 存储以出现次数为键的新字典：O(n)
# 3. 存储排序的键列表和结果列表：
# key为O(m) result为O(m) flat_result为O(k)

from collections import defaultdict
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # 1. 统计每个元素出现的次数
        count=defaultdict(int)
        for item in nums:
            count[item]+=1
        # 2. 调转一下key和value
        index_dict=defaultdict(list)
        for key in count:
            index_dict[count[key]].append(key)
        # 3. 排序（这里是对m个元素进行排序，因此时间复杂度是O(mlogm)）
        key=list(index_dict.keys())
        key.sort(reverse=True) # reverse=True表示按照降序输出   
        result=[]
        for freq in key:
            result.append(index_dict[freq])
            if len(result)>=k:
                break
        # 4. 扁平化结果列表
        flat_result=[item for sublist in result for item in sublist]
        return flat_result[0:k]