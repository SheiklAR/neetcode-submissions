class PrefixTree:

    def __init__(self):
        self.trie = {}
        

    def insert(self, word: str) -> None:
        def dfs(i, place):
            print('in', place)
            if i >= len(word):
                return
            key = word[i]
            if key not in place:
                place[key] = {}

            next_place = place[key]
            dfs(i+1, next_place)
            if i == len(word) - 1:
                next_place['isEnd'] = True
        
        dfs(0, self.trie)
        print('trie', self.trie)


    def search(self, word: str) -> bool:
        i = 0
        n = len(word)
        d = self.trie

        while i < n:
            char = word[i]

            if char not in set(d.keys()):
                return False
             
            d = d[char]
            i += 1

        return 'isEnd' in d and d['isEnd']

        

    def startsWith(self, prefix: str) -> bool:

        i = 0
        n = len(prefix)
        d = self.trie

        while i < n:
            char = prefix[i]

            if char not in set(d.keys()):
                return False
            d = d[char]
            i += 1

        return True
        