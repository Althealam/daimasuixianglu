class Solution:
    def reverseWords(self, s: str) -> str:
        string_list = list(s.split())
        left, right = 0, len(string_list)-1
        while left<=right:
            string_list[left], string_list[right] = string_list[right], string_list[left]
            left+=1
            right-=1
        return ' '.join(string_list)
        