import collections


class Node:
    def __init__(self):
        self.kid = collections.defaultdict(Node)
        self.isword = False


class Trie:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        cur = self.root
        for w in word:
            cur = cur.kid[w]
        cur.isword = True

    def search(self, word: str) -> bool:
        cur = self.root
        for w in word:
            cur = cur.kid.get(w)
            if not cur:
                return False
        return cur.isword

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for w in prefix:
            cur = cur.kid.get(w)
            if not cur:
                return False
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
