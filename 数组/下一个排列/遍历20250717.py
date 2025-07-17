# 注意：本题要求原地修改，也就是空间复杂度只能是O(1)
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)

        # 第一步：从右向左找到第一个小于右侧相邻数字的数nums[i]
        i = n-2
        while i>=0 and nums[i]>=nums[i+1]:
            i-=1
        
        # 如果找到了，进入第二步；否则跳过第二步，反转整个数组
        if i>=0:
            # 第二步：从右向左找到nums[i]右边最小的大于nums[i]的数nums[j]
            j=n-1
            while nums[j]<=nums[i]:
                j-=1
            nums[i], nums[j] = nums[j], nums[i]
        
        # 第三步：反转nums[i+1:]
        # nums[i+1:]=nums[i+1:][::-1]这样写也可以，但是空间复杂度不是O(1)的
        left, right = i+1, n-1
        while left<right:
            nums[left], nums[right] = nums[right], nums[left]
            left+=1
            right-=1