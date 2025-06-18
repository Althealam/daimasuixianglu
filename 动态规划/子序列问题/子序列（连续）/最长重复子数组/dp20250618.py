# 1. dp数组以及下标的含义：dp[i][j]表示以nums1[i-1]为结尾和以nums2[j-1]为结尾的最长重复子数组的长度
# 2. 递推公式
# 如果nums1[i-1]==nums2[j-1]: dp[i][j]=dp[i-1][j-1]+1
# 3. 初始化：全部初始化为0
# 4. 遍历顺序：从前向后遍历
nums1 = list(map(int, input().split()))
nums2 = list(map(int, input().split()))

def ditui(nums1, nums2):
    dp=[[0]*(len(nums2)+1) for _ in range(len(nums1)+1)]
    result=0
    for i in range(1, len(nums1)+1):
        for j in range(1, len(nums2)+1):
            if nums1[i-1]==nums2[j-1]:
                dp[i][j]=dp[i-1][j-1]+1
            result=max(result, dp[i][j])
    return result

result=ditui(nums1, nums2)
print(result)