# 思路：
# 1. 定义哈希表，存储每个元素的出现次数
# 2. 定义桶，桶的key是元素的出现次数，value是元素值
# 3. 倒序遍历桶，找到前面k个元素值

# 时间复杂度：O(n)
# 空间复杂度：O(n)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 1. 定义哈希表，存储每个元素的出现次数
        hash_map = collections.defaultdict(int)
        for num in nums:
            if num not in hash_map:
                hash_map[num]=1
            else:
                hash_map[num]+=1
        max_cnt = max(hash_map.values()) # 最大出现次数

        # 2. 将出现次数相同的元素，放到同一个桶中
        buckets = [[] for _ in range(max_cnt+1)]
        for x, c in hash_map.items():
            buckets[c].append(x)
        
        # 3. 倒序遍历buckets，将出现次数前k大的元素加入答案
        ans = []
        for bucket in buckets[::-1]:
            ans +=bucket
            # 由于答案唯一，一定会出现恰好等于k的情况
            if len(ans)==k:
                return ans
        