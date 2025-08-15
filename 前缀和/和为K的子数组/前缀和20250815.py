# 连续子数组问题：使用前缀和转化
# 前缀和的定义：s[0] = 0, s[i]=nums[0]+nums[1]+nums[i-1]
# 如果i<j，如果nums[i]到nums[j-1]的元素和为k，那么s[j]-s[i] = k
# 问题转化：s中有多少下标(i, j)满足i<j并且s[j]-s[i]=k==>如果二重循环遍历，那么时间复杂度过高
# 因此转化为s[i]=s[j]-k==>遍历s，枚举右边的j，统计左边有多少个i满足i<j并且s[i]-s[j]=k

# 时间复杂度：O(n)
# 空间复杂度：O(n)
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # 计算前缀和数组
        s = [0]*(len(nums)+1)
        for i, x in enumerate(nums):
            s[i+1] = s[i]+x
        
        ans = 0
        cnt = defaultdict(int)
        for sj in s:
            ans+=cnt[sj-k]
            cnt[sj]+=1 # 计算i的数量
        return ans
        