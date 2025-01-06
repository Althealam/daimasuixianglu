# 思路：
# 1. 对nums排序
# 2. i遍历nums，j遍历nums，计算nums[i]+nums[j]（让j<i）
# left=i+1, right=j-1，计算nums[left]+nums[right]+nums[i]+nums[j]，判断是否为target
# （1）nums[left]+nums[right]+nums[i]+nums[j]<target：left+=1
# （2）nums[left]+nums[right]+nums[i]+nums[j]>target：right-=1
# （3）nums[left]+nums[right]+nums[i]+nums[j]=target: result.append(...)
# 剪枝：
# （1）nums[j]>target and nums[j]>0 and target>0
# （2）nums[left]==nums[left-1]
# （3）nums[right]==nums[right+1]
# （4）nums[i]+nums[j]>target and target>0
# 时间复杂度：O(n^3)
# 空间复杂度：O(m)，其中m是满足四数之和的组合数量

class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        result=[]
        # 顺序是j,i,left,right
        for j in range(len(nums)):
            # 对j剪枝
            if nums[j]==nums[j-1] and j>=1:
                continue
            # 剪枝
            if nums[j]>0 and nums[j]>target and target>0:
                break
            for i in range(j+1,len(nums)):
                # 剪枝
                if nums[i]+nums[j]>target and target>0:
                    break
                # 对i剪枝
                if nums[i]==nums[i-1] and i>j+1: # 注意这里是i>j+1
                    continue
                right=len(nums)-1
                left=i+1
                while left<right:
                    sum=nums[left]+nums[right]+nums[i]+nums[j]
                    if sum==target:
                        result.append([nums[j],nums[i],nums[left],nums[right]])
                        # 对left进行剪枝
                        while left<right and nums[left]==nums[left+1]:
                            left+=1
                        # 对right进行剪枝
                        while left<right and nums[right]==nums[right-1]:
                            right-=1
                        # 注意：不管有没有剪枝，都要移动这个
                        left+=1
                        right-=1
                    elif sum>target:
                        right-=1
                    elif sum<target:
                        left+=1
        return result
                
            

        