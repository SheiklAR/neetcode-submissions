class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s1) > len(s2):
            return False
        
        d_s1 = defaultdict(int)
        d_s2 = defaultdict(int)
        for c in s1:
            d_s1[c] += 1

        # print(d_s1)
        #for every window check frequency of the s1 in s2 if both same:
        #return True
        def add_char_count(string, char):
            d_s2[char] = string.count(char)

        n = len(s2)

        cur = ''
        for c in s2:
            cur += c
            print(cur)
            add_char_count(cur, c)
            print(d_s2)
            if d_s1 == d_s2:
                return True
            
            if len(cur) == len(s1):
                d_s2[cur[0]] -= 1
                if d_s2[cur[0]] == 0:
                    del d_s2[cur[0]]
                cur = cur[1:]
                print('deleted current',cur)



        return False