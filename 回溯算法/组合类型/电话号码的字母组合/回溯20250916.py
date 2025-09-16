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
        path = []
        if len(digits)==0:
            return res
        self.traversal(res, path, digits, self.letter_map, 0)
        return res
    
    def traversal(self, res, path, digits, letter_map, startIndex):
        if len(path)==len(digits):
            res.append(''.join(path[:]))
            return
        index = int(digits[startIndex])
        letters = letter_map[index]
        for letter in letters:
            path.append(letter)
            self.traversal(res, path, digits, letter_map, startIndex+1)
            path.pop()
        