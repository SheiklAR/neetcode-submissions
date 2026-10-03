class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        
        stack = deque([beginWord])
        level = 1
        visited = {beginWord}

        def isOneCharDiff(word1, word2):
            # print(word1, word2)
            cnt = 0
            N = len(word1)
            i = 0
            while i < N:
                if word1[i] != word2[i]:
                    cnt += 1
                i += 1
            return cnt == 1


        while stack:
            n = len(stack)

            for _ in range(n):
                w = stack.popleft()

                for word in wordList:
                    if word in visited:
                        continue
                    if isOneCharDiff(w, word):
                        # print(w, word)
                        if word == endWord:
                            return level + 1

                        visited.add(word)
                        stack.append(word)
                    
            level += 1

            if not stack:
                return 0