from itertools import product

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
#         # My solution 1: Brute force
#         result = 0        
#         height_sorted = sorted(set(height), reverse=True)
#         hashmap = {unique_i: [idx for idx, i in enumerate(height) if i == unique_i] for unique_i in height_sorted}
                
#         # pick the longest verticals first. Brute force iterate max areas.
#         for y1, y2 in product(height_sorted, height_sorted):
#             y_min = min(y2, y1)
#             xs = [x1 - x2 for x1, x2 in product(hashmap[y1],hashmap[y2]) if x1 - x2 > 0]
#             if len(xs) == 0:
#                 continue
#             this_max_area = max([y_min * x for x in xs])            
#             result = max(result, this_max_area)
        
#         return result

        # Leetcode solution: 2-pointer approach
        result = 0
        left = 0
        right = len(height) - 1
        
        while left < right:
            area = (right - left) * min(height[left], height[right])
            result = max(result, area)
            
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        
        return result

        
# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the container contains the most water.

# Return the maximum amount of water a container can store.

# Notice that you may not slant the container.


