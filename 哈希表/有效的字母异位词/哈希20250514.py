class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_s=defaultdict(int)
        dict_t=defaultdict(int)
        for i in s:
            dict_s[i]+=1
        for i in t:
            dict_t[i]+=1
        return dict_s==dict_t