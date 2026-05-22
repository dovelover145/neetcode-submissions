class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

class WordDictionary:

    def __init__(self):
       self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.word = True
        

    def search(self, word: str) -> bool:
        def searchAux(word, cur):
            if not word:
                return True if cur.word else False
            
            c = word[0]
            if c == ".":
                for child in list(cur.children.values()):
                    if searchAux(word[1:], child):
                        return True
                return False
            else:
                if c in cur.children:
                    return searchAux(word[1:], cur.children[c])
                return False
        
        return searchAux(word, self.root)
        
