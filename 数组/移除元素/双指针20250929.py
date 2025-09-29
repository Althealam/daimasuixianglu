# 思路：定义快慢指针fast和slow，fast的作用是指向不是val的元素，slow的作用是进行覆盖
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        slow, fast = 0, 0
        while fast<len(nums): # fast用来指向不等于val的元素
            if nums[fast]!=val:
                nums[slow] = nums[fast]
                slow+=1
            fast+=1
        return slow