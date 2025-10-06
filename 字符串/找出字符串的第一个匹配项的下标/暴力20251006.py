class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return -1
        if len(needle)>len(haystack):
            return -1
        for i in range(len(haystack)-len(needle)+1): # iterate haystack, want to find needle from the index i
            match = True
            for j in range(len(needle)): # iterate needle
                if haystack[i+j]!=needle[j]: 
                    match = False
                    break
            if match: # iterate all needle and determine whether it is match
                return i
        return -1