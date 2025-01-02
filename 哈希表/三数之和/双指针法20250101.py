# 方法：双指针法（有点类似滑动窗口法）
# 思路：首先对nums进行排序，判断nums[0]是否大于0，如果是的话直接返回False（因为数组已经排序了，这种情况下不可能为0）
# 用i遍历nums，然后让left为i+1，right为len(nums)-1
# 其次，判断nums[i]+nums[left]+nums[right]的和
# 1. nums[i]+nums[left]+nums[right]<0: left+=1
# 2. nums[i]+nums[left]+nums[right]=0: result.append([i,left,right])
# 3. nums[i]+nums[left]+nums[right]>0: right-=1
# 注意点： 1. a+b+c=0 2. 不重复的三元组

# 时间复杂度：
# 1. 排序操作：O(nlogn)
# 2. 遍历nums：O(n)
# 3. 内层双指针：O(n)
# 总的时间复杂度：O(nlogn)+O(n)+O(n)=O(n^2)
# 空间复杂度：
# 1. result的空间占用：O(k)（k为满足条件的三元组个数）
# 2. 排序：O(logn) python的排序算法一般是原地排序，但是会使用递归调用栈来作为辅助空间
# 总的空间复杂度：O(k)

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result=[]
        nums.sort()
        for i in range(len(nums)):
            if nums[i]>0:
                return result
            left=i+1
            right=len(nums)-1
            # 1. 去重i
            if nums[i]==nums[i-1] and i>0:
                continue
            while left<right:
                sum=nums[i]+nums[left]+nums[right]
                if sum==0:
                    result.append([nums[i],nums[left],nums[right]])
                    # 找到了，则开始去重
                    # 2. 去重right（right要往左边找）
                    while nums[right]==nums[right-1] and left<right:
                        right-=1
                    # 3. 去重left（left要往右边找）
                    while nums[left]==nums[left+1] and left<right:
                        left+=1
                    right-=1
                    left+=1
                elif sum<0:
                    left+=1
                elif sum>0:
                    right-=1
        return result
                


        