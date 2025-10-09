class Solution:
    def jump(self, nums: List[int]) -> int:
        step = 0 # the step need to achieve the len(nums)-1
        cur_distance = 0 # current maximal distance
        next_distance = 0 # next maximal distance
        for i in range(len(nums)-1):
            next_distance = max(next_distance, i+nums[i])
            if i==cur_distance: # already achieve the maximal distance now
                cur_distance=next_distance # update the next maximal distance
                step+=1 # need to another step
        return step
                
