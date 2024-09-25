
class TrieNode:
    def __init__(self):
        self.children = {}
        self.count = 0
        
class Trie:
    def __init__(self):
        self.trie = TrieNode()

    def insert(self, word):
        node = self.trie
        
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.count +=1
            
            
    def word_count(self, word):
        node = self.trie
        total_count = 0
        for char in word:
            if char not in node.children:
                return total_count
            
            node = node.children[char]
            total_count += node.count
        return total_count
        
        
    #     def word_count(self, word):
    #         node = self.trie
    #         total_count = 0
    #         for char in word:
    #             total_count += node.children[char].count
    #             node = node.children[char]

    #         return total_count


class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        trie =  Trie()
        
        for word in words:
            trie.insert(word)
            
            
        
        
        
        return [trie.word_count(word) for word in words ]
        
        
        
        
#-------------------------------------------------------------------        
        
        
#         #brute force  O(n)??
#         #build a hash map of all prefix for each word, add +1 on every aperance
        
        
#         prefix_aperance = Counter()
        
#         for w in words:
#             for prefix in [w[:i+1] for i in range(len(w))]:
#                 prefix_aperance[prefix] +=1
                
#         #print(prefix_aperance)
        
#         ans = [0]*len(words)
#         for i,w in  enumerate(words):
#             for prefix in [w[:i+1] for i in range(len(w))]:
#                 ans[i] +=prefix_aperance[prefix] 
                
#         return ans
            
            