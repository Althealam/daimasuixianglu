### 将数组nums拆分为等和的k个子数组

class Solution:
    def chaifenshuzu(self, nums, k):
        total_sum = sum(nums)
        if total_sum%k!=0:
            return False
        target = total_sum//k
        res = []
        visited = [0]*len(nums)
        self.traversal(res, [], 0, nums, k, visited, target, 0)
        return len(res)==k
    
    def traversal(self, res, path, startIndex, nums, k, visited, target, current_sum):
        if len(res)==k:
            return 
        if current_sum == target:
            res.append(path[:])
            self.traversal(res, [], 0, nums, k, visited, target, 0)
            return
        if current_sum>target:
            return 
        for i in range(startIndex, len(nums)):
            if visited[i]==1:
                continue
            visited[i]=1
            path.append(nums[i])
            self.traversal(res, path, i+1, nums, k, visited, target, current_sum+nums[i])
            path.pop()
            visited[i]=0

nums = [1,2,3,0,3]
k = 3
sol = Solution()
res = sol.chaifenshuzu(nums, k)
print(res)