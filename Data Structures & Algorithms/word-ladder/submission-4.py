class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        adj = defaultdict(set)

        def changesByOne(word1, word2):
            cnt = 0
            for i in range(len(word1)):
                if word1[i] != word2[i]:
                    cnt += 1
                if cnt > 1:
                    return False

            return cnt == 1
        


        
        if changesByOne(beginWord, wordList[0]):
            adj[beginWord].add(wordList[0])
        

        for i in range(len(wordList)):
            word1 = wordList[i]
            for j in range(i+1, len(wordList)):
                word2 = wordList[j]

                if changesByOne(word1, word2):
                    adj[word1].add(word2)
                    adj[word2].add(word1)
                
                if changesByOne(word2, beginWord):
                    adj[beginWord].add(word2)
            
        ans = float('inf')
        path = set()

        # @cache
        def dfs(word, cnt):
            nonlocal ans
            if word == endWord:
                ans =  min(cnt + 1, ans)
                return
            
            path.add(word)
            for nei in adj[word]:
                if nei not in path:
                    dfs(nei, cnt + 1)
            
            path.remove(word)

        
        dfs(beginWord, 0)
        return 0 if ans == float('inf') else ans