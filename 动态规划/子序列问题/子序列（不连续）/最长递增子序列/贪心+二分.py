# 思路：维护一个列表tails，这个列表tails记录了当前找到的不同长度递增子序列的最小尾部元素
# 通过遍历nums中的每个元素，利用二分查找确定元素在tails中的合适位置，然后更新tails列表

# 时间复杂度：O(nlogn)
# 1. 遍历输入列表nums：O(n)
# 2. 二分查找：对于nums列表中的每个元素，代码使用二分查找来确定元素在tails列表中的合适位置 二分查找的时间复杂度为O(logm)，其中m是tails的长度

# 空间复杂度：O(n)
# 1. tails列表的空间开销：tails列表用于存储当前找到的最长递增子序列的可能尾部元素，其长度不超过n

def solution(nums):
    tails=[] # 用来记录最长递增子序列

    for num in nums:
        # 使用二分法查找在tails中第一个大于等于num的位置（二分查找合适的插入位置）
        left=0
        right=len(tails)-1

        while left<right:
            mid=(left+right)//2
            if tails[mid]<num: # 说明num应该插入到mid的位置之后
                left=mid+1
            else: # 说明num可以替换mid位置的元素
                right=mid

        # 根据二分查找结果更新tails列表
        # 如果left等于tails的长度，说明num比tails中的所有元素都大，则将其添加到tails末尾
        if left==len(tails):
            tails.append(num)
        # 否则，更新tails中第一个大于等于num的元素为num
        else:
            tails[left]=num
        
    return tails