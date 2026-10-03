# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from heapq import heappush, heappop

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return 
        

        heap = []
        cnt = 0

        for node in lists:
            if node: # n log k as heap will alway be of size k
                cnt += 1
                heappush(heap, (node.val, cnt, node))
        

        node = ListNode()
        ans = node

        while heap:
            num,c,new = heappop(heap)
            # new = ListNode(num)
            if new.next:
                cnt += 1
                heappush(heap, (new.next.val, cnt, new.next))

            new.next = None
            node.next = new
            

            node = node.next
        
        return ans.next

        # n log n
        # if not lists:
        #     return 

        
        # num_list = []

        # for node in lists:
        #     n = node

        #     while n:
        #         heappush(num_list, n.val)
        #         n = n.next
        

        # node = ListNode()
        # ans = node

        # while num_list:
        #     num = heappop(num_list)
        #     new = ListNode(num)
        #     node.next = new
        #     node = node.next
        
        # return ans.next




        # temp = []

        # node = lists[0]

        # while node:
        #     temp.append(node.val)
        #     node = node.next


        # def merge(arr1, arr2):
        #     i, j = 0, 0
        #     res = []

        #     while i < len(arr1) and j < len(arr2):
        #         # print(type(arr1), type(arr2))
        #         if arr1[i] < arr2[j]:
        #             res.append(arr1[i])
        #             i += 1
        #         else:
        #             res.append(arr2[j])
        #             j += 1
            
        #     res.extend(arr1[i:])
        #     res.extend(arr2[j:])

        #     return res


        # for n in lists[1:]:
        #     node = n

        #     cur = []

        #     while node:
        #         cur.append(node.val)
        #         node = node.next


        #     temp = merge(temp, cur)
        

        # node = ListNode()
        # ans = node

        # for n in temp:
        #     new = ListNode(n)
        #     node.next = new
        #     node = node.next

        # return ans.next
