digits = str(input())

class Solution:
    def __init__(self):
        self.letter_map={
            2: "abc",
            3: "def",
            4: "ghi",
            5: "jkl",
            6: "mno",
            7: "pqrs",
            8: "tuv",
            9: "wxyz"
        }

    def sol(self, digits):
        result=[]
        path=[]
        if len(digits)==0:
            return result
        self.traversal(result, path, digits, self.letter_map, 0)
        return result

    def traversal(self, result, path, digits, letter_map, startIndex):
        if len(path)==len(digits):
            result.append(''.join(path[:]))
            return 
        index = int(digits[startIndex])
        letters = letter_map[index]
        for letter in letters:
            path.append(letter)
            self.traversal(result, path, digits, letter_map, startIndex+1)
            path.pop()
    
sol = Solution()
print(sol.sol(digits))