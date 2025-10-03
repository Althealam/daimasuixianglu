class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hash_map = [0]*26
        for s in magazine:
            hash_map[ord(s)-ord('a')]+=1
        for s in ransomNote:
            hash_map[ord(s)-ord('a')]-=1
        for i in range(26):
            if hash_map[i]<0:
                return False
        return True
