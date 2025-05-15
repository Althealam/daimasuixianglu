# 思路：
# 1. 定义一个hashmap，计算nums1和nums2的相加之和与出现次数
# 2. 遍历nums3和nums4，如果0-nums3[i]-nums4[j]在hashmap中出现过的话，则统计出现的次数
class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        hashmap={}
        for num1 in nums1:
            for num2 in nums2:
                if num1+num2 not in hashmap:
                    hashmap[num1+num2]=1
                else:
                    hashmap[num1+num2]+=1
        
        # 检查-(n3+n4)是否出现在hashmap中
        count=0 # 返回次数
        for num3 in nums3:
            for num4 in nums4:
                key=-num3-num4
                if key in hashmap:
                    count+=hashmap[key]
        return count
        