
SUGGESTION_NUM = 10 # num of suggestions for each node          

class Suggestions:

  def __init__(self):
    self.suggestions = [ (0, None) for _ in range(SUGGESTION_NUM) ]

  def add(self, suggestion, frequency):
    i = next( (i for i, v in enumerate(self.suggestions) if frequency > v[0]), None)
    if i is not None:
      self.suggestions[i] = (frequency, suggestion)
    self.suggestions.sort()

  def all(self):
    return [ w for _, w in self.suggestions if w is not None ]

class Trie:

    def __init__(self, parent=None):
        self.is_word = 0
        self.suggestions = Suggestions()
        self.parent = parent
        self.children = {}

    def update_frequencies(self, word, frequency):
      cur = self
      while cur.parent is not None:
        cur = cur.parent
        cur.suggestions.add(word, frequency)
            
    def insert_trie(self, word, i):
        if i == len(word):
            self.is_word += 1
            self.update_frequencies(word, self.is_word)
            return
        first_char = word[i]
        self.children.setdefault(first_char, Trie(self))
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
        return node

def build_tree(file):
  tree = Trie()
  with open(file) as f:
    for l in f.readlines():
      tree.insert(l[:-1])
  return tree









        

