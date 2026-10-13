class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if s1 > s2:
            return False
        
        d_s1 = defaultdict(int)
        for c in s1:
            d_s1[c] += 1

        #for every window check frequency of the s1 in s2 if both same:
        #return True
        n = len(s2)

        cur = ''
        for c in s2:
            cur += c
            d_s2 = Counter(cur)
            if d_s1 == d_s2:
                return True
            
            if len(cur) == len(s1):
                cur = cur[1:]

        return False