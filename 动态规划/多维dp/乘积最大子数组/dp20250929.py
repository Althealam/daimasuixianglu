# 右端点下标为i的子数组的最大乘积为fmax[i]，右端点下标为i的子数组的最小乘积为fmin[i]
# 递推公式：
# 对于nums[i]:
# （1）如果nums[i]单独为一个子数组：nums[i]
# （2）nums[i]和前面的子数组拼接起来：fmax[i] = fmax[i-1]*nums[i]
# fmax[i] = max(fmax[i-1]*nums[i], fmin[i-1]*nums[i], nums[i])
# fmin[i] = min(fmax[i-1]*nums[i], fmin[i-1]*nums[i], nums[i])
# 初始化：fmax[0] = fmin[0] = nums[0]
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        f_max = [0]*len(nums)
        f_min = [0]*len(nums)
        f_max[0] = f_min[0] = nums[0]
        for i in range(1, len(nums)):
            f_max[i] = max(f_max[i-1]*nums[i], f_min[i-1]*nums[i], nums[i])
            f_min[i] = min(f_max[i-1]*nums[i], f_min[i-1]*nums[i], nums[i])
        return max(f_max)

        