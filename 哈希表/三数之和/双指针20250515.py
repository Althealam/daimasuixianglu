# 思路：
# 1. 将数组排序
# 2. 定义三个指针：i, left, right（left=i+1, right=len(nums)-1）
# 3. 计算sum_=nums[i]+nums[left]+nums[right]
# （1）sum_>0: right-=1
# （2）sum_<0: left+=1
# （3）sum_==0: ans.append([i, left, right])
# 剪枝：
# （1）nums[i]>0 那么nums[left]>0 nums[right]>0==>nums[left]+nums[right]+nums[i]>0 
# （2）相同元素：i>0 and nums[i]==nums[i-1]
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans=[]
        for i in range(len(nums)):
            if nums[i]>0:
                return ans
            if i>0 and nums[i]==nums[i-1]:
                continue
            left=i+1
            right=len(nums)-1
            while right>left:
                sum_=nums[i]+nums[left]+nums[right]
                if sum_>0:
                    right-=1
                elif sum_<0:
                    left+=1
                else:
                    ans.append([nums[i], nums[left], nums[right]])
                    while right>left and nums[right]==nums[right-1]:
                        right-=1
                    while right>left and nums[left]==nums[left+1]:
                        left+=1
                    right-=1
                    left+=1

        return ans
        