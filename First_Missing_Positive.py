# https://leetcode.com/problems/first-missing-positive/description/

from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        "make a set -> iterate"
        set_nums = sorted(set(nums))

        cnt = 1
        for num in set_nums:
            if num < 1:
                continue

            if cnt != num:
                return cnt
            
            cnt += 1

        return cnt


nums = [100000, 3, 4000, 2, 15, 1, 99999]

obj = Solution()
print(obj.firstMissingPositive(nums))