class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        cnt = Counter()
        left = 0
        max_length = 0
        for right, c in enumerate(s):
            cnt[c]+=1
            while cnt[c]>2:
                cnt[s[left]]-=1
                left+=1
            max_length = max(max_length, right-left+1)
        return max_length