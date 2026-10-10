class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        adj = defaultdict(set)
        wordList = set(wordList)

        def changesByOne(word1, word2):
            cnt = 0
            for i in range(len(word1)):
                if word1[i] != word2[i]:
                    cnt += 1
                if cnt > 1:
                    return False

            return cnt == 1
        


        
        # if changesByOne(beginWord, wordList[0]):
        #     adj[beginWord].add(wordList[0])
        

        # for i in range(len(wordList)):
        #     word1 = wordList[i]
        #     for j in range(i+1, len(wordList)):
        #         word2 = wordList[j]

        #         if changesByOne(word1, word2):
        #             adj[word1].add(word2)
        #             adj[word2].add(word1)
                
        #         if changesByOne(word2, beginWord):
        #             adj[beginWord].add(word2)
        

        length = 0

        dq = deque([beginWord])
        visit = set()
        visit.update(adj[beginWord])


        while dq:
            length += 1

            for _ in range(len(dq)):
                node = dq.popleft()
                if node == endWord:
                    return length
                
                word = list(node)
                for i in range(len(word)):
                    curr = word[i]
                    for c in range(97, 97 + 26):
                        if c != curr:
                            word[i] = chr(c)
                            new_word = ''.join(word)
                            if new_word not in visit and new_word in wordList:
                                visit.add(new_word)
                                dq.append(new_word)
                            word[i] = curr

                
        

        return 0
