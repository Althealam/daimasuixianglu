# 思路：遍历prices数组，维护最小价格，每次都求解能够赚到的最大值

prices = list(map(int, input().split()))

def ditui(prices):
    result=0
    min_price = float('inf')
    for i in range(len(prices)):
        min_price = min(min_price, prices[i])
        result = max(result, prices[i]-min_price)
    return result

result=ditui(prices)
print(result)