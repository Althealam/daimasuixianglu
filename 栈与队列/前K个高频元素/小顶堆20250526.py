# 思路：使用堆，堆是一个完全二叉树，树中每个节点的值都不小于（或者不大于）其左右孩子的值
# （1）父亲节点大于等于左右孩子：大顶堆 （2）父亲节点小于等于左右孩子：小顶堆
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map_={} # 统计元素的出现频率
        for i in range(len(nums)):
            map_[nums[i]]=map_.get(nums[i], 0)+1
        
        # 对频率排序
        # 定义小顶堆，大小为k
        pri_que=[] # 小顶堆

        # 用固定大小为k的小顶堆，扫描所有频率的数值
        for key, freq in map_.items():
            heapq.heappush(pri_que, (freq, key))
            if len(pri_que)>k: # 如果堆的大小大于K，则队列弹出
                heapq.heappop(pri_que)
        
        # 找出前K个高频元素
        result=[0]*k
        for i in range(k-1, -1, -1):
            result[i]=heapq.heappop(pri_que)[1]
        return result

        