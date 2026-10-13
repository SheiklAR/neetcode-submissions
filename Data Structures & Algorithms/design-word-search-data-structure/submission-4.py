class WordDictionary:

    def __init__(self):
        self.trie = {}
        

    def addWord(self, word: str) -> None:
        d = self.trie
        for c in word:
            if c not in d:
                d[c] = {}
            d = d[c]

        d['IsEnd'] = True

    def search(self, word: str) -> bool:
        n = len(word)
        d = self.trie

        print(word)
        def bt(i,dd):
            if i == n:
                return dd.get('IsEnd', False)

            if word[i] == '.':
                # dd = dd[k]
                for k in dd.keys():
                    if not bt(i + 1, dd[k]):
                        return False
                return True
                
            else:
                if word[i] not in dd:
                    return False
                
                # dd = dd[word[i]]
                if not bt(i+1, dd[word[i]]):
                    return False
            
                return True
        # alphabets = 'abcdefghijklmnopqrstuvwxyz'

        # return 

        return bt(0,d)
