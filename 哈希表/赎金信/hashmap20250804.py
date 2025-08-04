class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hashmap = [0]*26
        for i in magazine:
            hashmap[ord(i)-ord('a')]+=1
        for j in ransomNote:
            hashmap[ord(j)-ord('a')]-=1
            if hashmap[ord(j)-ord('a')]<0:
                return False
        return True
        
        