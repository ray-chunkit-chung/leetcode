# My solution

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """        
        # Merge two lists
        merged = sorted(nums1 + nums2)
        
        # Find median
        idx = len(merged)/2        
        if len(merged) % 2 == 0:
            # list len even. Take avg of middle two
            result = (merged[idx] + merged[idx - 1]) / 2.0
        else:
            # list len odd. Take middle one
            result = float(merged[idx])

        return result
