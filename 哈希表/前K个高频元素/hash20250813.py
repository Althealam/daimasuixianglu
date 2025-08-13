# 1. 定义哈希表，存储每个元素的出现次数
# 2. 将哈希表反过来，找到出现次数最高的TopK个元素值
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import defaultdict
        hash_map = defaultdict(int)
        for i, x in enumerate(nums):
            if x not in hash_map:
                hash_map[x]=1
            else:
                hash_map[x]+=1
        max_cnt = max(hash_map.values()) # 找到最高的答案值

        buckets = [[] for _ in range(max_cnt+1)]
        for num, cnt in hash_map.items():
            buckets[cnt].append(num)
        
        ans = []
        for bucket in buckets[::-1]:
            ans+=bucket
            if len(ans)==k:
                return ans
                
        