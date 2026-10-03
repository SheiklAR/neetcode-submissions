class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        ans = ""
        t_count = Counter(t)

        start_ind = -1
        #find the start:
        for i in range(len(s)):
            c = s[i]
            if c in t_count:
                start_ind = i
                break
        
        if start_ind == -1:
            return ""
        
        def hasTheRightCounts():
            for key in t_count.keys():
                if cur_count[key] < t_count[key]:
                    return False
            return True
        
        def findNext(string):
            for i in range(1, len(s)):
                c = s[i]
                if c in t_count:
                    return i

        s = s[start_ind:]
        cur_count = defaultdict(int)
        cur = ""
        for c in s:
            cur += c
            if c in t_count:
                cur_count[c] += 1
                if hasTheRightCounts():
                    if ans == "":
                        ans = cur
                    else:
                        ans = ans if len(ans) < len(cur) else cur

                    print(ans)
                    
                    shrink = True

                    while shrink:
                        next_ind = findNext(s)
                        prev = cur[0]

                        cur_count[prev] -= 1

                        cur = cur[next_ind: ]

                        if cur_count[prev] < t_count[prev]:
                            break
                        else:
                            ans = ans if len(ans) < len(cur) else cur

                        # print(next_ind, cur[next_ind:])



        return ans