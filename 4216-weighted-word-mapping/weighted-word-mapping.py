class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:

        hash_letters_normal = { i:ch for i,ch in enumerate(ascii_lowercase[::-1])  }
        hash_letters_weights = { ch:w for ch,w in  zip(ascii_lowercase,weights) }

        def findVal(word):
            ans = 0
            for ch in word:
                ans+= hash_letters_weights[ch]
            return ans%26
        

        ans = []
        for word in words:
            ans.append(  hash_letters_normal[findVal(word)]   )

        return "".join(ans)
