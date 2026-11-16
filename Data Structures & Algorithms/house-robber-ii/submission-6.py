class Solution:
    def rob(self, nums: List[int]) -> int:
        N = len(nums)

        if N <= 3:
            return max(nums)
        
        def rob(arr1):
            # print(arr1)
            # start = [False] * N
            start1 = start2 = True
            start3 = False
            arr1[2] += arr1[0]
            
            for i in range(3, N):
                if i == N-1:
                    p1, p2 = 0, 0
                    if not start1:
                        p1 = arr1[i-2]
                    if not start2:
                        p2 = arr1[i-3]
                    
                    arr1[i] = max(arr1[i], arr1[i] + p1, arr1[i] + p2)

                    # print(arr1)
                    # print(arr1[i])
                    return arr1


                # print(arr1[i])
                if arr1[i-2] + nums[i] > arr1[i-3] + nums[i]:
                    # start[i] = start[i-2]
                    start3 = start2
                    arr1[i] += arr1[i-2]
                else:
                    # start[i] = start[i-3]
                    start3 = start1
                    arr1[i] += arr1[i-3]
                
                start1, start2 = start2, start1


        return max(max(rob(nums[:])), max(rob(nums[::-1])))