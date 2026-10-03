class Solution:
    def trap(self, height: List[int]) -> int:
        h = len(height)
        left_water = []
        right_water = []
        ans = 0

        def contain_water(arr, container): 
            arr_h = None
            for hi in arr:
                # hi = arr[i]
                if arr_h == None:
                    #can't hold any water
                    container.append(0)
                    arr_h = hi
                else:
                    if hi > arr_h:
                        arr_h = hi
                        container.append(0)
                    else:
                        container.append(arr_h - hi)

        contain_water(height, left_water)
        contain_water(reversed(height), right_water)

        # right_h = None
        # for hr in reversed(height):
            # hi = height[i]
            # if right_h == None:
            #     #can't hold any water
            #     right_water.append(0)
            #     right_h = hi
            # else:
            #     if hi > right_h:
            #         right_h = hi
            #         right_water.append(0)
            #     else:
            #         right_water.append(right_h - hj)

        # right_water.reverse()

        for l,r in zip(left_water, reversed(right_water)):
            ans += min(l, r)
        
        return ans
        # if h < 2:
        #     return 0
        
        # l,r = None, None
        # ans = 0
        
        # lh = 3
        # #left,  0,0,2,0,2,3,4,0
        # rh = 3

        
        # #right, 3,1,2,0,2,3,2,0,0,0,

        # ans = (0+0+2+0+2+3+2,)

        # #till add the water in the container to the cur_water if
        # #container found add it to the solution

        # for i in range(h):
        #     if height[i] > 0:
        #         l = i
        
        # cur_level = 0
        # for j in range(i+1, h):
        #     cur_level += abs(height[j] - height[l])

        #     if (j - l) + 1 > 1


