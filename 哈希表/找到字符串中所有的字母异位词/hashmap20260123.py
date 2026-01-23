# 1. Step1: get the hashmap from p
# 2. Step2: iterate the hash map from s
class Solution:
    def findAnagrams(self, s: str, p: str):
        hash_map_p = [0]*26
        ans = []
        for st in p:
            hash_map_p[ord(st)-ord('a')]+=1
        for i in range(0, len(s)-len(p)+1):
            hash_map_p_copy = hash_map_p.copy()
            slice_s = s[i:i+len(p)]
            print(slice_s)
            for j in slice_s:
                hash_map_p_copy[ord(j)-ord('a')]-=1
            if hash_map_p_copy == [0]*26:
                ans.append(i)
        return ans

s = "beeaaedcbc"
p = "c"
solution = Solution()
print(solution.findAnagrams(s, p))