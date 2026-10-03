class WordDictionary:

    def __init__(self):
        self.d = {}
        

    def addWord(self, word: str) -> None:
        cur = self.d
        for c in word:
            if c not in cur:
                cur[c] = {}
            cur = cur[c]
        cur['#'] = True


    def search(self, word: str) -> bool:
        # nodes = self.d

        def dfs(s, nodes):
            for i in range(s, len(word)):
                c = word[i]
                if c == '.':
                    for node in nodes:
                        if node != '#':
                            if dfs(i+1, nodes[node]):
                                return True
                    return False
                
                else:
                    if c not in nodes:
                        return False
                    nodes = nodes[c]
            
            return '#' in nodes

        return dfs(0, self.d)

    
        
