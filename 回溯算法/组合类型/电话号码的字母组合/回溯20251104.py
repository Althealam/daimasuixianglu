class Solution:
    def __init__(self):
        self.letter_map = {
            2: "abc",
            3: "def",
            4: "ghi",
            5: "jkl",
            6: "mno",
            7: "pqrs",
            8: "tuv",
            9: "wxyz"
        }

    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        self.traversal(res, [], digits, 0)
        return res

    
    def traversal(self, res, path, digits, startIndex):
        if len(path)==len(digits):
            res.append(''.join(path[:]))
            return 
        s = self.letter_map[int(digits[startIndex])]
        for ch in s:
            path.append(ch)
            self.traversal(res, path, digits, startIndex+1)
            path.pop()
