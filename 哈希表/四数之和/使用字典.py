# 方法：使用字典
# 思路：和三数之和类似，但是新增加一个k，遍历k和i，然后同样定义一个left和right
# 使得nums[k]+nums[i]+nums[left]+nums[right]=target
# 注意：
# 1. 剪枝操作：nums里的数和target都可以是负数，因此不能和三数之和一样，直接使用nums[k]>target来做剪枝
# （1）【一级剪枝】修改为 if nums[k]>0 and nums[k]>target and target>0: return False
# （2）【二级剪枝】if nums[k]+nums[i]>target and nums[right]>0 and nums[left]>0: break
# 2. 去重
# （1）【一级去重】对k进行去重：if k>0 and nums[k]==nums[k-1]: continue
# （2）【二级去重】对i进行去重：if i>k+1 and nums[i]==nums[i-1]: continue（其中i=k+1）

# 时间复杂度：O(n^3) 当i、j和k对nums进行遍历时，产生时间复杂度

class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # 创建一个字典来存储输入列表中每个数字的频率
        freq={}
        for num in nums:
            freq[num]=freq.get(num,0)+1
        
        # 创建一个集合来存储最终答案，并遍历4个数字的所有唯一组合
        ans=set()
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                for k in range(j+1,len(nums)):
                    val=target-(nums[i]+nums[j]+nums[k])
                    if val in freq:
                        # 确保没有重复
                        count=(nums[i]==val)+(nums[j]==val)+(nums[k]==val)
                        if freq[val]>count:
                            ans.add(tuple(sorted([nums[i],nums[j],nums[k],val])))
        
        return [list(x) for x in ans]