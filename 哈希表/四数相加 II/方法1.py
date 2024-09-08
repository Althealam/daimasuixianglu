# 方法：使用字段存储nums1和nums2中的元素及其和
# 注意：不需要去重，并且是求解数量即可，不用输出位置
# 思路：遍历A和B，存储A和B的所有值a+b，放到一个集合里，然后在C和D里找有没有出现-(a+b)，有的话就计数加一
# 利用map解决该题，遍历A和B时用value存储出现的次数，key存储和
# 遍历C和D的时候，判断是否有-(c+d)出现在上述map中，如果有的话cnt就加上对应的value值
# 先遍历A、B，再遍历C、D：O(2n^2)（分别遍历A、B和C、D时时间复杂度都是n^2）
# 先遍历A，再遍历B、C、D：O(n^3)
class Solution(object):
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :type nums4: List[int]
        :rtype: int
        """
        hashmap=dict()
        # 在字典中，dict={
        #    'key1': 'value1',
        #    'key2': 'value2',
        #    ...
        #} 同时，key是唯一的
        # 首先遍历nums1和nums2
        for n1 in nums1:
            for n2 in nums2:
                if n1+n2 in hashmap:
                    hashmap[n1+n2]+=1 # 统计出现的次数 
                else:
                    hashmap[n1+n2]=1
        
        # 其次遍历nums3和nums4
        count=0 # 初始化次数
        for n3 in nums3:
            for n4 in nums4:
                target=-(n3+n4) # 判断nums3和nums4的-(n3+n4)是否在哈希表中出现过
                if target in hashmap:
                    count+=hashmap[target] # hashmap[target]就是出现的次数
        return count