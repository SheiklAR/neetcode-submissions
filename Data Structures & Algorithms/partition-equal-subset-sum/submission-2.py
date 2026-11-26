class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        
        if sum(nums) % 2 > 0: return False
        half = sum(nums) / 2
        visited = set()
        seen = set()
        sum_ = 0

        def dfs():
            nonlocal sum_
            # print(visited)
            # key = None
            if visited:
                print(visited)
                print(list(visited))
                key = tuple(sorted(list(visited)))

                if key in seen:
                    return False
                
                seen.add(key)

            # if visited and key in seen:
            #     return False
            # nonlocal sum_
            print(sum_)

            # seen.add(key)

            if sum_ > 0 and sum_ == half:
                return True


            for i in range(len(nums)):
                if i not in visited:
                    visited.add(i)
                    sum_ += nums[i]
                    if dfs():
                        return True
                    
                    visited.remove(i)
                    sum_ -= nums[i]
            
            return False
                    

        return dfs()
        