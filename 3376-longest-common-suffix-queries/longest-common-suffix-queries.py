class MyTrieNode:
    def __init__(self):
        self.children = {}
        self.indx = float("inf")
        self.min_size = float("inf")

class MyTrie:
    def __init__(self):
        self.root = MyTrieNode()


    def insert(self,indx,word):
        curr = self.root

        if len(word) < curr.min_size:
            curr.min_size = len(word)
            curr.indx = indx
        
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = MyTrieNode()
            curr = curr.children[ch]
            if len(word) < curr.min_size:
                curr.min_size = len(word)
                curr.indx = indx



    def query(self,word):
        curr = self.root

        for ch in word:
            if ch not in curr.children:
                break
            else:
                curr = curr.children[ch]

        return curr.indx


        

class Solution:
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:

        myTrie = MyTrie()

        for i,word in enumerate(wordsContainer):
            myTrie.insert(i, word[::-1])
    
        ans = [0]*len(wordsQuery)
        for i,word in enumerate(wordsQuery):
            ans[i] = myTrie.query(word[::-1])

        return ans



        