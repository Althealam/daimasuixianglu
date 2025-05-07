# 思路：
# 1. 先按照h降序排序，如果h相同的，则将k小的放在前面（lambda x的x[0]表示升序排序）
# 2. 按照k进行插入操作 
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda x: (-x[0], x[1]))
        que=[] # 结果队列
        for p in people:
            que.insert(p[1], p) # 按照p[1]进行插入操作，插入的元素为p
        return que