
# 思路：使用堆，堆是一个完全二叉树，树中每个节点的值都不小于（或者不大于）其左右孩子的值
# （1）父亲节点大于等于左右孩子：大顶堆 （2）父亲节点小于等于左右孩子：小顶堆
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 统计每个元素出现的次数
        time_dict=defaultdict(int)
        for num in nums:
            time_dict[num]+=1

        # 更改字典，key为出现次数，value为数字的集合
        index_dict=defaultdict(list)
        for key in time_dict:
            index_dict[time_dict[key]].append(key)
        
        # 排序
        key=list(index_dict.keys())
        key.sort()

        result=[]
        cnt=0
        # 获取前面k项
        while key and cnt!=k:
            result+=index_dict[key[-1]]
            cnt+=len(index_dict[key[-1]])
            key.pop()
        return result[0:k]