# 方法：双指针法
# 思路：和三数之和类似，但是新增加一个k，遍历k和i，然后同样定义一个left和right
# 使得nums[k]+nums[i]+nums[left]+nums[right]=target
# 注意：
# 1. 剪枝操作：nums里的数和target都可以是负数，因此不能和三数之和一样，直接使用nums[k]>target来做剪枝
# （1）【一级剪枝】修改为 if nums[k]>0 and nums[k]>target and target>0: return False
# （2）【二级剪枝】if nums[k]+nums[i]>target and nums[right]>0 and nums[left]>0: break
# 2. 去重
# （1）【一级去重】对k进行去重：if k>0 and nums[k]==nums[k-1]: continue
# （2）【二级去重】对i进行去重：if i>k+1 and nums[i]==nums[i-1]: continue（其中i=k+1）

# 时间复杂度：O(n^2) 当i和j对nums进行遍历时，产生时间复杂度

class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort() # 对数组进行排序
        n=len(nums)
        result=[]
        for i in range(n):
            # 【一级剪枝】
            if nums[i]>target and nums[i]>0 and target>0:
                break
            # 【一级去重】
            if i>0 and nums[i]==nums[i-1]:
                continue
            for j in range(i+1,n):
                # 【二级剪枝】
                if nums[i]+nums[j]>target and target>0:
                    break
                # 【二级去重】
                if j>i+1 and nums[j]==nums[j-1]:
                    continue
                left=j+1 # 定义左指针
                right=n-1 # 定义右指针
                while left<right:
                    s=nums[i]+nums[j]+nums[left]+nums[right] # 四数之和
                    if s==target:
                        result.append([nums[i],nums[j],nums[left],nums[right]])
                        while left<right and nums[left]==nums[left+1]:
                            left+=1
                        while left<right and nums[right]==nums[right-1]:
                            right-=1
                        left+=1 # 继续遍历
                        right-=1
                    elif s<target: 
                        left+=1
                    elif s>target:
                        right-=1
        return result