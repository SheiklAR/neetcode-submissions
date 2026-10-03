class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        words = set(wordDict)
        d = {}



        #if the cur word in dict
        #dfs check for next word
        #if next word comes true, we return true #cache it
        #else return false # also cache it

        #base case -> if reached the end of the word and the word not in  the  list return false else return true
        def dfs(start):
            if start in d:
                return d[start]
            # print(start)
            cur_word = ''
            for i in range(start, n):
                cur_word += s[i]
                #base case
                if i == n - 1:
                    # print(cur_word)
                    if cur_word in words:
                        return True
                    else:
                        return False

                if cur_word in words:
                    if dfs(i + 1):
                        d[i+1] = True
                        return True
                    else:
                        d[i+1] = False

            d[start] = False
            return False

        return dfs(0)
