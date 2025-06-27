n = int(input())
k = int(input())

class Solution:
    def sol(self, n, k):
        result = []
        path = []
        self.traversal(result, path, n, k, 1)
        return result

    def traversal(self, result, path, n, k, startIndex):
        if len(path)==k:
            result.append(path[:])
            return 
        for i in range(startIndex, n+1):
            path.append(i)
            self.traversal(result, path, n, k, i+1)
            path.pop()

s = Solution()
print(s.sol(n, k))