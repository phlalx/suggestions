          
class Trie:

    def __init__(self, is_word=False, children=None):
        self.is_word = is_word
        if children:
            self.children = children
        else:
            self.children = {}
            
    def insert_trie(self, word, i):
        if i == len(word):
            self.is_word = True
            return
        first_char = word[i]
        self.children.setdefault(first_char, Trie())
        node = self.children[first_char]
        node.insert_trie(word, i + 1)

    def search_trie(self, word, i):
        if i == len(word):
            return self
        first_char = word[i]
        node = self.children.get(first_char) 
        return node.search_trie(word, i + 1) if node else None
    
    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        self.insert_trie(word, 0)

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        node = self.search_trie(word, 0)
        return node.is_word if node else False

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        node = self.search_trie(prefix, 0)
        return bool(node)

def build_tree(file):
  tree = Trie()
  with open(file) as f:
    for l in f.readlines():
      tree.insert(l[:-1])
  return tree

