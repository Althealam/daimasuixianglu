# 1. dp数组以及下标的含义：dp[i][j]表示以[i, j]为右下角，并且只包含1的正方形边长
# 2. 递推公式
# （1）matrix[i][j]=0: dp[i][j]=0
# （2）matrix[i][j]!=0: dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])+1
# 3. 初始化：全部初始化为0，初始化dp[0][j]和dp[i][0]
# 4. 遍历顺序：从上到下 从左到右
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        dp = [[0]*(len(matrix[0])) for _ in range(len(matrix))]
        res = float('-inf')
        for i in range(len(matrix)):
            if int(matrix[i][0]) ==1:
                dp[i][0] = 1
                res = max(res, dp[i][0])
        
        for j in range(len(matrix[0])):
            if int(matrix[0][j]) ==1:
                dp[0][j] = 1
                res = max(res, dp[0][j])
        
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if int(matrix[i][j])==1:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) +1
                    res = max(res, dp[i][j])
        
        return res*res if res!=float('-inf') else 0
        