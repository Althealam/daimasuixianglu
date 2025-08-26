class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda x: (-x[0], x[1])) # 按照x[0]升序排序，按照x[1]降序排序（x[0]为身高，x[1]为前面有x[1]个人的身高大于等于x[0]）
        que = []
        for p in people:
            que.insert(p[1], p) # 在p[1]的位置插入p
        return que
        