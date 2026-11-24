class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # "string", d = ["st", "ring"]
        dic = set(wordDict)
        dp = {}

        def get_the_index(index_string):
            # print(index_string)
            for i in range(len(index_string)-1, -1, -1):
                # print('here')
                if index_string[i] == '-':
                    return int(index_string[i+1:])
        

        def dfs(w, string_index):
            if string_index in dp:
                return dp[string_index]

            i = get_the_index(string_index)

            if i >= len(s):
                if not w:
                    return True
                else:
                    return False

            res1 = False
            res2 = False

            if w + s[i] in dic:
                # 'word' in dic
                res1 = dfs('', '-' + str(i+1))
            res2 = dfs(w + s[i], string_index +'-' + str(i+1))



            dp[string_index] = res1 or res2
            return res1 or res2
        
        return dfs('', '-' + '0')