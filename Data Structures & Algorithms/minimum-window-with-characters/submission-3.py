class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        ans = ""

        #if we find the answer for substring that is > len(t) then
        #there is a possiblity of less than that.

        #approach
        #count the t
        #iterate untill you find a char in t (which means starting of the shortest subs)
        #increase the window and check for the remaining t's
        #add it to the answer
        #look for shorter substring by keep shrinking the window 
        #( expand if the removing char costs shrinking actual string
        #compensate by expanding the widnow
        #)
        #exactly where wherever the next char in the t appears

        #once we reached em now it's time for other values

        t_count = Counter(t)

        start_ind = -1
     
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