# 题目：给定x和y，查找x^y>y^x的个数
# 暴力法
def count_pairs(arr1, arr2):
    count=0
    for x in arr1:
        for y in arr2:
            if x**y>y**x:
                count+=1
    return count

