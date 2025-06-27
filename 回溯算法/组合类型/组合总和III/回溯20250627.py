k = int(input())
n = int(input())

class Solution:
    def sol(self, n, k):
        result = []
        path = []
        self.traversal(result, path, n, k, 1)
        return result

    def traversal(self, result, path, n, k, startIndex):
        if len(path)==k and sum(path)==n:
            result.append(path[:])
            return 
        for i in range(startIndex, 10):
            path.append(i)
            self.traversal(result, path, n, k, i+1)
            path.pop()

sol = Solution()
print(sol.sol(n, k))