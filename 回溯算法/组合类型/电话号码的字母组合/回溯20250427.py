class Solution:
    def __init__(self):
        self.letters_map={
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'qprs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits)==0:
            return []
        result=[]
        path=[]
        self.traversal(result, path, digits, 0, self.letters_map)
        return result
    
    def traversal(self, result, path, digits, startIndex, letters_map):
        if len(path)==len(digits):
            result.append(''.join(path[:]))
            return 
        index=digits[startIndex]
        letters=letters_map[index]
        for letter in letters:
            path.append(letter)
            self.traversal(result, path, digits, startIndex+1, letters_map)
            path.pop()
