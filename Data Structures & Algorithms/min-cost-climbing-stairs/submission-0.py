class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        cache = {}
        n = len(cost)
        cache[n] = 0
        cache[n+1] = 0
        #cache

        #from every stage we may wanna check the i+1, i+2

        #we can start at 0,1

        def bt(i):
            if i in cache:
                return cache[i]
            
            if i >= n:
                return 0
            
            s1 = bt(i+1)
            s2 = bt(i+2)
            print(s1, s2)

            min_cost = cost[i] + min(s1, s2)
            cache[i] = min_cost

            return min_cost

        return min(bt(0), bt(1))
