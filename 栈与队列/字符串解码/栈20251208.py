class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        res = ""
        k = 0 # the replication count for current string
        for st in s:
            if "0"<=st<="9":
                k=k*10+int(st)
            elif st=='[': # we need store the strings we need to replicate
                stack.append((res, k)) # we store the previous strings and the count that this strings need to replication
                res, k = "", 0 # we need to reset them, otherwise it will still all the thing
            elif st==']': # we have already iterate all string we need to replicate
                last_res, last_k = stack.pop() # pop the res and k
                res = last_res+res*last_k 
            else: # iterate string
                res+=st
        return res
