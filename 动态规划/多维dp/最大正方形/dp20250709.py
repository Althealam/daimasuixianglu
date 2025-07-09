# 1. dp数组以及下标的含义：dp[i][j]表示以[i,j]为右下角，并且只包含1的正方形的边长的最大值
# 2. 递推公式：
# （1）matrix[i][j]=0: dp[i][j]=0
# （2）matrix[i][j]!=0：dp[i][j]由dp[i-1][j], dp[i][j-1], dp[i-1][j-1]共同决定
# dp[i][j]=min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])+1
# 3. 初始化：全部初始化为0 dp[0][j], dp[i][0]=1 if matrix[i][j]==1
# 4. 遍历顺序：从上到下 从左到右
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        dp=[[0]*len(matrix[0]) for _ in range(len(matrix))]
        
        result = float('-inf')
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]=='1':
                    if i==0 or j==0:
                        dp[i][j]=1
                    else:
                        dp[i][j]=min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])+1
                result = max(result, dp[i][j])
        return result*result if result!=float('-inf') else 0
        
        