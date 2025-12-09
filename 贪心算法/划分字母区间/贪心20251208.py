class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # store the last appearance for every string
        last_appearance = {}
        for i in range(len(s)):
            last_appearance[s[i]] = i
        res = []
        start = 0
        end = 0
        for i in range(len(s)):
            end = max(end, last_appearance[s[i]])
            if i==end:
                res.append(end-start+1)
                start = i+1
        return res
        