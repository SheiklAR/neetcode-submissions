class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        stack = deque([])
        ans = []

        #approach
        #using store the values which are greater than the last elements in the stack
        #this way, we confirm that max element of the subarray at that positions at the starting of the stack
        #pop if the cur elements is greater than elements in the stack.

        '''
        nums=[1,2,1,0,4,2,6]
        k=3

        Your Output:

        [2,1,4,4,6]
        Copy
        Expected output:

            [2,2,4,4,6]
        '''


        for i,num in enumerate(nums):
            if stack:
                if i - stack[0][1] == k:

                    stack.popleft()

                while stack and stack[-1][0] <= num:
                    stack.pop()
                
            stack.append((num,i))

            if i+1 >= k:
                ans.append(stack[0][0])

  
        return ans