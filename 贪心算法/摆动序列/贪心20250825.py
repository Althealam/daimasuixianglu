class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums)<=1:
            return len(nums)
        curdifff= 0 # 当前一对元素的差值
        prediff = 0 # 之前一对元素的差值
        result = 1 # 峰值的个数
        for i in range(len(nums)-1):
            curdiff = nums[i+1]-nums[i]
            if (prediff<=0 and curdiff>0) or (prediff>=0 and curdiff<0):
                result+=1
                prediff = curdiff
        return result
        