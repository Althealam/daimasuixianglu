class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = [0]*len(nums)
        left, right = 0, len(nums)-1
        ind = len(nums)-1
        while left<=right:
            if nums[left]*nums[left]<=nums[right]*nums[right]:
                res[ind] = nums[right]*nums[right]
                right-=1
            else:
                res[ind] = nums[left]*nums[left]
                left+=1
            ind -=1
        return res
        