class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_map = [0]*26
        for i in s:
            hash_map[ord(i)-ord('a')]+=1
        for j in t:
            hash_map[ord(j)-ord('a')]-=1
        for i in range(26):
            if hash_map[i]!=0:
                return False
        return True
        