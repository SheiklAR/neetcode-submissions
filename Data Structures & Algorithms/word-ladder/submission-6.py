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
            

        length = 1

        dq = deque(list(adj[beginWord]))
        visit = set()
        visit.update(adj[beginWord])


        while dq:
            length += 1

            for _ in range(len(dq)):
                node = dq.popleft()
                if node == endWord:
                    return length
                
                for nei in adj[node]:
                    if nei not in visit:
                        visit.add(nei)
                        dq.append(nei)
        

        return 0
