# 思路：两个维度的确定
# 1. 先排身高h，按照身高从大到小排，如果身高相同，则将k小的放在前面
# 2. 再排数量k
# （1）局部最优：按身高高的人的k来进行插入，插入操作过后的人满足队列属性（按照k来插入即可，k就是他要插入的位置）
# （2）全局最优：最后都做完插入操作，整个队列都满足题目属性

# 时间复杂度：O(n)
# 空间复杂度：O(n)

class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        # 1. 先按照身高从大到小排序（people是[h,k]的形式）
        people.sort(key=lambda x: (-x[0], x[1])) # (-x[0],x[1])表示按照h从大到小排序，按照k从小到大排序
        
        # 2. 按照数量进行插入，从左到右进行处理
        result=[]
        for p in people:
            result.insert(p[1], p) # 将元素p插入到result的p[1]位置
        return result

        