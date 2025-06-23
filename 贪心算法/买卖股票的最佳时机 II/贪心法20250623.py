prices = list(map(int, input().split()))

def greedy(prices):
    result = 0
    for i in range(1, len(prices)):
        if prices[i]-prices[i-1]>0:
            result+=prices[i]-prices[i-1]
    return result