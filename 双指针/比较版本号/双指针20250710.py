# 时间复杂度：O(n)
# 空间复杂度：O(n)
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        list1 = version1.split('.')
        list2 = version2.split('.')
        i, j = 0, 0
        while i<len(list1) or j<len(list2):
            v1 = int(list1[i]) if i<len(list1) else 0
            v2 = int(list2[j]) if j<len(list2) else 0
            if v1<v2:
                return -1
            if v1>v2:
                return 1
            i+=1
            j+=1
        return 0
        