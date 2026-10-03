class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        seen = set()
        seen_list = deque([])

        ans = 0

        for c in s:
            print(c)
            print(seen_list)
            if c not in seen:
                seen.add(c)
                # seen_list.append(c)
            else:
                #if we have seen it remove until c also from seen
                while c != seen_list[0]:
                    popped = seen_list.popleft()
                    seen.remove(popped)
                seen_list.popleft()
            seen_list.append(c)

            ans = max(ans, len(seen_list))

        return ans
