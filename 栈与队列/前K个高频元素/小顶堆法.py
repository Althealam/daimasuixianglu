# 思路：使用大顶堆和小顶堆
# 大顶堆和小顶堆底层是一个二叉树
# 大顶堆指的是头部的元素都要比孩子的元素大（根节点是最大的）
# 小顶堆指的是头部的元素都要比孩子的元素小（根节点是最小的）
# 利用map存储nums里所有元素出现的频次，k为nums的值，value为出现的次数
# 我们应该利用小顶堆来找前k个高频的元素
# 为什么不适用大顶堆？定义一个大小为k的大顶堆，在每次移动更新大顶堆的时候，每次弹出都把最大的元素弹出去了，那么没办法保留下来前k个高频元素
# 我们使用小顶堆，因为要统计前k个元素，只有小顶堆每次将最小的元素弹出，然后小顶堆里积累的才是前k个最大元素


# 分析：
# 1. 要统计元素出现频率
# 2. 对频率排序
# 3. 找出前k个高频元素

# 时间复杂度：O(nlogn)
# 1. 统计数字出现次数：O(n)
# 2. 根据出现次数分组：O(m) m是不同数字的数量，最坏情况下为O(n)
# 3. 排序出现次数：key.sort()需要对出现次数进行排序，时间复杂度为O(mlogm)
# 4. 获取前k项：while key and cnt!=k: O(m)
# 总的时间复杂度为O(n+mlogm+m) 简化为O(nlogn)
# 空间复杂度：O(n+k)
# 1. 统计数字出现次数：time_dict字典存储了所有数字以及其出现次数O(m)
# 2. 根据出现次数分组：index_dict字典存储了每个出现次数对应的数字集合 O(m)
# 3. 排序出现次数：排序操作本身不需要额外的空间
# 4. 结果列表：result列表存储了最终的前k个高频数字，空间复杂度为O(k)

import heapq

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # 要统计元素出现频率
        map_={} # nums[i]:对应出现的次数
        for i in range(len(nums)):
            map_[nums[i]]=map_.get(nums[i],0)+1
        
        # 对频率排序
        # 定义一个小顶堆，大小为k
        pri_que=[] # 小顶堆

        # 用固定大小为k的小顶堆，扫描所有频率的数值
        for key, freq in map_.items():
            heapq.heappush(pri_que,(freq, key))
            if len(pri_que)>k: # 如果堆的大小大于k，则队列弹出，保证堆的大小一直为k
                heapq.heappop(pri_que)

        # 找出前k个高频元素，因为小顶堆先弹出的是最小的
        result=[0]*k
        for i in range(k-1,-1,-1):
            result[i]=heapq.heappop(pri_que)[1]
        return result