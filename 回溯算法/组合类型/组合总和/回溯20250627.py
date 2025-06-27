candidates = list(map(int, input().split()))
target = int(input())

class Solution:
    def sol(self, candidates, target):
        result = []
        path = []
        self.traversal(candidates, target, result, path, 0)
        return result

    def traversal(self, candidates, target, result, path, startIndex):
        if sum(path)==target:
            result.append(path[:])
            return 
        if sum(path)>target:
            return 
        for i in range(startIndex, len(candidates)):
            path.append(candidates[i])
            self.traversal(candidates, target, result, path, i)
            path.pop()

sol = Solution()
print(sol.sol(candidates, target))