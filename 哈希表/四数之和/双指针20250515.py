# 思路：
# 1. 定义i, j, left, right j=i+1 left=j+1 right=len(nums)-1
# 2. sum_=nums[i]+nums[j]+nums[left]+nums[right]
# sum_>0: right-=1
# sum_<0: left+=1
# sum_==0: ans.append([nums[i], nums[j], nums[left], nums[right]])
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        ans=[]
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if i>0 and nums[i]==nums[i-1]:
                    continue
                if j>i+1 and nums[j]==nums[j-1]:
                    continue
                left=j+1
                right=len(nums)-1
                while left<right:
                    sum_=nums[i]+nums[j]+nums[left]+nums[right]
                    if sum_>target:
                        right-=1
                    elif sum_<target:
                        left+=1
                    else:
                        ans.append([nums[i], nums[j], nums[left], nums[right]])
                        while left<right and nums[left]==nums[left+1]:
                            left+=1
                        while left<right and nums[right]==nums[right-1]:
                            right-=1
                        left+=1
                        right-=1
        return ans

        