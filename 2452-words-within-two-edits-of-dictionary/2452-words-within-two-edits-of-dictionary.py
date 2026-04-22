from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

    def add_letter(self, letter):
        if letter not in self.children:
            self.children[letter] = TrieNode()


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add_word(self, word):
        node = self.root
        for letter in word:
            node.add_letter(letter)
            node = node.children[letter]
        node.is_word = True

    def search(self, word, node=None, edits=0, index=0):
        if node is None:
            node = self.root

        # reached the end of the word
        if index == len(word):
            return node.is_word and edits <= 2

        current_letter = word[index]

        for child_letter, child_node in node.children.items():
            next_edits = edits + (child_letter != current_letter)

            if next_edits <= 2:
                if self.search(word, child_node, next_edits, index + 1):
                    return True

        return False


class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        trie = Trie()

        for word in dictionary:
            trie.add_word(word)

        ans = []

        for word in queries:
            if trie.search(word):
                ans.append(word)

        return ans