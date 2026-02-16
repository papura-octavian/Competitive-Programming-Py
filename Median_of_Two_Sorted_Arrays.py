from typing import List

# https://leetcode.com/problems/median-of-two-sorted-arrays/

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        s = sorted(nums1 + nums2)

        if len(s) % 2:
            return s[len(s) // 2]
        
        return (s[len(s) // 2] + s[len(s) // 2 - 1]) / 2
        
nums1 = [2,2,4,4]
nums2 = [2,2,2,4,4]

obj = Solution()
print(obj.findMedianSortedArrays(nums1, nums2))