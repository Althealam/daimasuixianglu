# 思路：前缀和思路，求出所有大于等于0的元素之和
prices = list(map(int, input().split()))

def ditui(prices):
    diff=[0]*(len(prices)-1)
    for i in range(len(prices)-1):
        diff[i]=prices[i+1]-prices[i]
    return sum(i for i in diff if i>=0)

result=ditui(prices)
print(result)