class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        cache = {}
        #DFS
        #iterate
        #add next or not => if next added compute the sum of rest, cache it
        #if they are equal => return True

        ans = False

        def sum_list(arr):
            sum_ = 0
            for index in arr:
                sum_ += nums[index]
            return sum_

        def get_rest_indices(arr):
            rest_indexes = []
            for i in range(n):
                if i not in arr:
                    rest_indexes.append(i)
            return rest_indexes

        def dfs(cur):
            if len(cur) == n:
                return False    
            key = tuple(cur)
 
            cur_sum = sum_list(cur)
            rest_indices = get_rest_indices(cur)

            rest_sum = None

            if tuple(rest_indices) in cache:
                rest_sum = cache[tuple(rest_indices)]
            else:
                rest_sum = sum_list(rest_indices)

            if rest_sum == cur_sum:
                print(cur, rest_indices)
                print(cur_sum, rest_sum)
                return True
            
            for i in range(cur[-1] + 1, n):
                cur.append(i)
                result = dfs(cur)
                if result == True:
                    return True
                cur.pop()
            
            cache[key] = cur_sum
            cache[tuple(rest_indices)] = rest_sum



        for i in range(n):
            if dfs([i]):
                return True
        
        return False






















