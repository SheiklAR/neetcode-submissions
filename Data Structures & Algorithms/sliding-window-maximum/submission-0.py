class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        stack = deque([])
        ans = []
        #approach

        #using store the values which are greater than the last elements in the stack

        #this way, we confirm that max element of the subarray at that positions at the starting of the stack

        #pop if the cur elements is greater than elements in the stack.

        for i,num in enumerate(nums):
            if stack: 
                if len(stack) == k:
                    stack.popleft()

                while stack and stack[-1] <= num:
                    stack.pop()

            stack.append(num)
            if i+1 >= k:
                ans.append(stack[0])

        return ans