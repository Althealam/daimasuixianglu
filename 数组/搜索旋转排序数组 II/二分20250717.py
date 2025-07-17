# 思路：
# 1. 找到数组中的最小值
# 2. 判断target和nums[mid]的大小，来判断target的位置
# （1）target==nums[mid]: 直接return True
# （2）target>nums[mid]: target在第一段数组中，也就是[mid+1, right]
# （3）target<nums[mid]: target在第二段数组中，也就是[left, mid-1]
# 时间复杂度：O(logn)
# 空间复杂度：O(1)

class Solution:
    def find_min(self, nums):
        """寻找旋转点 也就是数组的最小值"""
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]: # mid在第一段数组中，也就是说最小值在[mid+1, right]中
                left = mid + 1
            elif nums[mid] < nums[right]: # mid在第二段数组中，也就是说最小值在[left, mid]中
                right = mid
            else: # 此时nums[mid]==nums[right]，无法确定mid在哪一段数组中
                # 关键修改：只在右边界与中间值相等时收缩右边界
                if nums[right - 1] > nums[right]:
                    return right  # 找到旋转点
                right -= 1 # 收缩有边界
        return left
    
    def search(self, nums: List[int], target: int) -> bool:
        if not nums:
            return False
        
        # 找到旋转点
        min_index = self.find_min(nums)
        
        # 确定搜索范围
        n = len(nums)
        left, right = 0, n - 1
        
        while left <= right:
            mid = (left + right) // 2
            # 计算实际索引（考虑旋转）
            real_mid = (mid + min_index) % n
            
            if nums[real_mid] == target: # 找到了target值
                return True
            elif nums[real_mid] < target: # target在第二段数组中，也就是[mid+1, right]
                left = mid + 1
            else: # target在第一段数组中，也就是[left, mid-1]
                right = mid - 1
        
        return False


