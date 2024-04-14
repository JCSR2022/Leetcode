class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWorld = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        word= word.strip().lower()
        currentNode = self.root
        
        for c in word:
            if c not in currentNode.children:
                currentNode.children[c] = TrieNode()
            currentNode = currentNode.children[c]
        currentNode.endOfWorld = True
        
        

    def search(self, word: str,currentNode = None) -> bool:
        word = word.strip().lower()
        if not currentNode: currentNode = self.root
        
        for i,c in enumerate(word):
            if c != '.':
                if c not in currentNode.children:
                    return False
                currentNode = currentNode.children[c]
            else:
                for cn in currentNode.children.values():
                    ans = self.search(word[i+1:],cn)
                    if ans == True:
                        return True
                return False  
        return currentNode.endOfWorld

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)