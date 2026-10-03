class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        c = candidates
        c.sort()
        n = len(c)
        ans = []

        def bt(arr, ind):

            sum_ = sum(arr)

            if sum_ == target:
                ans.append(arr[:])
                # print(ans)
                return
            
            if sum_ > target or ind >= n:
                return

            for i in range(ind, n):
                # if i > 0 and c[i] == c[i-1]:
                #     continue
                arr.append(c[i])
                bt(arr, i + 1)
                arr.pop()

        
        bt([], 0)

        anss = [tuple(x) for x in ans]
        anss = set(anss)

        ans = [list(x) for x in anss]
        return ans

