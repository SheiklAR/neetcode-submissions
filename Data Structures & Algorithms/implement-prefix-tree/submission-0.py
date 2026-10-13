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

        def dfs(i, place):
            print('se', place)
            if word[i] != place:
                return False
            
            if i == len(word) - 1:
                print('here')
                if 'isEnd' in place.keys():

                    return place['isEnd']
                else:
                    return False
                # return isEnd in place and place[isEnd]
            
            return dfs(i+1, place[i+1])
        
        return dfs(0, self.trie)

            


    def startsWith(self, prefix: str) -> bool:

        def dfs(i, place):
            print('sw', place)
            if prefix[i] != place:
                return False
            
            if i == len(prefix) - 1:
                return True
            
            return dfs(i+1, place[i+1])
        
        return dfs(0, self.trie)
        