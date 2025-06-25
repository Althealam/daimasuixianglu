# 思路： 
# 计算five, ten, twenty的张数，并且优先用ten找零，尽可能地保存five

nums = list(map(int, input().split()))

def greedy(nums):
    five, ten, twenty =0, 0, 0
    for item in nums:
        if item==5:
            five+=1
        elif item==10:
            if five>0:   
                ten+=1
                five-=1
            else:
                return False
        elif item==20:
            if ten>0 and five>0:
                ten-=1
                five-=1
                twenty+=1
            elif five>=3:
                five-=3
                twenty+=1
            else:
                return False
    return True
    