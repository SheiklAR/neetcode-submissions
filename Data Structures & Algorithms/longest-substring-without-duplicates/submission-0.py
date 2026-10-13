class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0

        seen = set()
        s_list = []

        for c in s:
            if not seen:
                # s_list.append(c)
                seen.add(c)
                ans = 1
                continue
            
            if c not in seen:
                # s_list.append(c)
                seen.add(c)
                ans = max(ans, len(seen))
            else:
                # seen.remove(c)

                # print(s_list)
                # print(seen)
                seen.clear()
                # s_list.clear()

                seen.add(c)
                # s_list.append(c)
        
        return ans

