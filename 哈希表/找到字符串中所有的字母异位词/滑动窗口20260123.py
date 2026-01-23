# 1. Step1: get the hashmap from p
# 2. Step2: iterate the hash map from s
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:   
        cnt_p = Counter(p)
        cnt_s = Counter()
        ans = []

        for right, c in enumerate(s):
            cnt_s[c]+=1 

            left = right-len(p)+1
            if left<0:
                continue
            if cnt_s==cnt_p:
                ans.append(left)
            cnt_s[s[left]]-=1
        return ans