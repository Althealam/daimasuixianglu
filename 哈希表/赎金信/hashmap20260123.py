class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hash_map = [0]*26
        for i in magazine:
            hash_map[ord(i)-ord('a')]+=1
        for j in ransomNote:
            hash_map[ord(j)-ord('a')]-=1
        for i in hash_map:
            if i<0:
                return False
        return True