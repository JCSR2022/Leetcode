class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWorld = False
        self.definition = None

class Trie:
    
    
    def __init__(self):
        self.root = TrieNode()
        
        
    def insert(self, word: str) -> None:
        word= word.strip().lower()
        currentNode = self.root
        
        for c in word:
            if c not in currentNode.children:
                currentNode.children[c] = TrieNode()
            currentNode = currentNode.children[c]
        currentNode.endOfWorld = True
        currentNode.definition = word
        
        
        
    def search(self, word: str) -> bool:
        word = word.strip().lower()
        currentNode = self.root
        for c in word:
            if c not in currentNode.children:
                return False
            currentNode = currentNode.children[c]
        return currentNode.endOfWorld 
        
        

    def startsWith(self, prefix: str) -> bool:
        prefix= prefix.strip().lower()
        currentNode = self.root
        for c in prefix:
            if c not in currentNode.children:
                return False
            currentNode = currentNode.children[c]
        return True
        
        
        
        
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)