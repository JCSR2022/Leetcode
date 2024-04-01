class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        if len(digits) == 0 :
            return []
        
        hashtable = {
            '2':"abc",
            '3':"def",
            '4':"ghi",
            '5':"jkl",
            '6':"mno",
            '7':"pqrs",
            '8':"tuv",
            '9':"wxyz"}
        
        vect = [hashtable[d] for d in digits]
        return [''.join(combination) for combination in product(*vect)]