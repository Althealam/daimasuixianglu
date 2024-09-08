# 使用字段和集合
# 方法：使用数组/set求解（如果没有限制数字<=1000，那就需要用set）
# 注意：直接使用set不仅占用空间比数组大，而且速度要比数组慢，set把数值映射到key上都要做hash计算的。
# 思路：将nums1变成哈希表的形式，然后再用nums2去遍历表，判断在这个哈希表里出现过的数字
# 时间复杂度：O(n+m) n是nums1的长度，m是nums2的长度
# 空间复杂度：O(n+k) n是nums1的长度，k是交集元素的数量
class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # 使用哈希表存储一个数组中的所有元素
        table={} # 空字段table，用于存储nums1中的元素
        for num in nums1:
            # table.get(num,0)
            # 检查table中是否存在num
            # 如果存在，返回与num相关联的值
            # 如果不存在，返回默认值+1
            table[num]=table.get(num,0)+1 # 如果它已经在table中，则将其计数增加1；如果它不在table中，则将其添加到table中，并设置计数为1.
        
        # 使用集合存储结果
        res=set()
        for num in nums2:
            if num in table:
                res.add(num) # 如果num在table中，就将其添加到集合res中
                del table[num] # 从table中删除num，这样在后续的遍历中就不会再添加到res中
            
        return list(res)